from flask import Blueprint, request, jsonify
from src.models.user import db
from src.models.room import Room, Participant

room_bp = Blueprint('room', __name__)

@room_bp.route('/rooms', methods=['POST'])
def create_room():
    """Crear una nueva sala"""
    try:
        data = request.get_json()
        if not data or 'name' not in data:
            return jsonify({'error': 'El nombre de la sala es requerido'}), 400
        
        room = Room(name=data['name'])
        db.session.add(room)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'room': room.to_dict(),
            'admin_url': f'/admin/{room.admin_code}',
            'invite_url': f'/join/{room.invite_code}'
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@room_bp.route('/rooms/admin/<admin_code>', methods=['GET'])
def get_room_admin(admin_code):
    """Obtener información de la sala para el administrador"""
    try:
        room = Room.query.filter_by(admin_code=admin_code).first()
        if not room:
            return jsonify({'error': 'Sala no encontrada'}), 404
        
        return jsonify({
            'success': True,
            'room': room.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@room_bp.route('/rooms/join/<invite_code>', methods=['GET'])
def get_room_info(invite_code):
    """Obtener información básica de la sala para unirse"""
    try:
        room = Room.query.filter_by(invite_code=invite_code).first()
        if not room:
            return jsonify({'error': 'Sala no encontrada'}), 404
        
        return jsonify({
            'success': True,
            'room': {
                'id': room.id,
                'name': room.name,
                'participant_count': len(room.participants)
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@room_bp.route('/rooms/join/<invite_code>', methods=['POST'])
def join_room(invite_code):
    """Unirse a una sala"""
    try:
        data = request.get_json()
        if not data or 'name' not in data:
            return jsonify({'error': 'El nombre es requerido'}), 400
        
        room = Room.query.filter_by(invite_code=invite_code).first()
        if not room:
            return jsonify({'error': 'Sala no encontrada'}), 404
        
        # Verificar si ya existe un participante con ese nombre en la sala
        existing_participant = Participant.query.filter_by(
            room_id=room.id, 
            name=data['name']
        ).first()
        
        if existing_participant:
            return jsonify({'error': 'Ya existe un participante con ese nombre en esta sala'}), 400
        
        participant = Participant(name=data['name'], room_id=room.id)
        db.session.add(participant)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'participant': participant.to_dict(),
            'room': {
                'id': room.id,
                'name': room.name,
                'is_shuffled': room.is_shuffled
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@room_bp.route('/rooms/admin/<admin_code>/shuffle', methods=['POST'])
def shuffle_room(admin_code):
    """Realizar el sorteo del amigo secreto"""
    try:
        room = Room.query.filter_by(admin_code=admin_code).first()
        if not room:
            return jsonify({'error': 'Sala no encontrada'}), 404
        
        if len(room.participants) < 2:
            return jsonify({'error': 'Se necesitan al menos 2 participantes para realizar el sorteo'}), 400
        
        if room.shuffle_participants():
            db.session.commit()
            return jsonify({
                'success': True,
                'message': 'Sorteo realizado exitosamente',
                'room': room.to_dict()
            }), 200
        else:
            return jsonify({'error': 'Error al realizar el sorteo'}), 500
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@room_bp.route('/participants/<participant_id>/secret-friend', methods=['GET'])
def get_secret_friend(participant_id):
    """Obtener el amigo secreto de un participante"""
    try:
        participant = Participant.query.get(participant_id)
        if not participant:
            return jsonify({'error': 'Participante no encontrado'}), 404
        
        room = participant.room
        if not room.is_shuffled:
            return jsonify({
                'success': True,
                'shuffled': False,
                'message': 'Aún no se ha realizado el sorteo. Esperando al administrador.'
            }), 200
        
        secret_friend = participant.get_secret_friend()
        if not secret_friend:
            return jsonify({'error': 'No se ha asignado amigo secreto'}), 404
        
        return jsonify({
            'success': True,
            'shuffled': True,
            'secret_friend': secret_friend.name,
            'participant': participant.name,
            'room': room.name
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@room_bp.route('/rooms/admin/<admin_code>/participants/<participant_id>', methods=['DELETE'])
def remove_participant(admin_code, participant_id):
    """Eliminar un participante de la sala (solo admin)"""
    try:
        room = Room.query.filter_by(admin_code=admin_code).first()
        if not room:
            return jsonify({'error': 'Sala no encontrada'}), 404
        
        participant = Participant.query.filter_by(id=participant_id, room_id=room.id).first()
        if not participant:
            return jsonify({'error': 'Participante no encontrado'}), 404
        
        db.session.delete(participant)
        
        # Si ya se había realizado el sorteo, hay que rehacerlo
        if room.is_shuffled:
            room.is_shuffled = False
            # Limpiar asignaciones de amigos secretos
            for p in room.participants:
                if p.id != participant_id:
                    p.secret_friend_id = None
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Participante eliminado exitosamente',
            'room': room.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

