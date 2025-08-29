from flask_sqlalchemy import SQLAlchemy
from src.models.user import db
import uuid
import random
import string

class Room(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    admin_code = db.Column(db.String(20), nullable=False, unique=True)
    invite_code = db.Column(db.String(20), nullable=False, unique=True)
    is_shuffled = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    # Relación con participantes
    participants = db.relationship('Participant', backref='room', lazy=True, cascade='all, delete-orphan')

    def __init__(self, name):
        self.name = name
        self.admin_code = self._generate_code()
        self.invite_code = self._generate_code()
        
    def _generate_code(self):
        """Genera un código único de 8 caracteres"""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    
    def shuffle_participants(self):
        """Realiza el sorteo del amigo secreto"""
        if len(self.participants) < 2:
            return False
            
        participant_list = list(self.participants)
        shuffled_list = participant_list.copy()
        
        # Asegurar que nadie se tenga a sí mismo
        while True:
            random.shuffle(shuffled_list)
            valid = True
            for i, participant in enumerate(participant_list):
                if participant.id == shuffled_list[i].id:
                    valid = False
                    break
            if valid:
                break
        
        # Asignar amigos secretos
        for i, participant in enumerate(participant_list):
            participant.secret_friend_id = shuffled_list[i].id
            
        self.is_shuffled = True
        return True

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'admin_code': self.admin_code,
            'invite_code': self.invite_code,
            'is_shuffled': self.is_shuffled,
            'participant_count': len(self.participants),
            'participants': [p.to_dict() for p in self.participants]
        }


class Participant(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    room_id = db.Column(db.String(36), db.ForeignKey('room.id'), nullable=False)
    secret_friend_id = db.Column(db.String(36), nullable=True)
    joined_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def get_secret_friend(self):
        """Obtiene el amigo secreto asignado"""
        if self.secret_friend_id:
            return Participant.query.get(self.secret_friend_id)
        return None

    def to_dict(self):
        secret_friend = self.get_secret_friend()
        return {
            'id': self.id,
            'name': self.name,
            'room_id': self.room_id,
            'secret_friend': secret_friend.name if secret_friend else None,
            'has_secret_friend': self.secret_friend_id is not None
        }

