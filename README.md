# likeFriends - Aplicación de Amigo Secreto

Una aplicación web completa para organizar intercambios de regalos de amigo secreto con tus amigos, familia o compañeros de trabajo.

## 🌟 Características

- **Creación de Salas**: Los administradores pueden crear salas de juego con códigos únicos
- **Invitaciones Fáciles**: Comparte enlaces o códigos de invitación para que otros se unan
- **Registro Simple**: Los participantes solo necesitan ingresar su nombre
- **Sorteo Automático**: El administrador puede realizar el sorteo con un clic
- **Visualización Segura**: Cada participante ve solo su amigo secreto asignado
- **Interfaz Moderna**: Diseño responsivo y atractivo con gradientes y animaciones
- **Despliegue en Línea**: Aplicación desplegada y accesible desde cualquier dispositivo

## 🚀 URL de la Aplicación Desplegada

**Aplicación en Línea**: https://p9hwiqcq8w7x.manus.space

## 📋 Funcionalidades Principales

### Para Administradores:
1. Crear nuevas salas de juego
2. Obtener enlaces de administración y códigos de invitación
3. Ver lista de participantes registrados
4. Realizar sorteo del amigo secreto
5. Eliminar participantes si es necesario
6. Volver a sortear si se requiere

### Para Participantes:
1. Unirse a salas usando códigos de invitación
2. Registrarse con solo su nombre
3. Ver su amigo secreto asignado después del sorteo
4. Recibir enlace personal para consultar su asignación

## 🛠️ Tecnologías Utilizadas

### Backend:
- **Flask**: Framework web de Python
- **SQLAlchemy**: ORM para base de datos
- **SQLite**: Base de datos ligera
- **Flask-CORS**: Manejo de CORS para API
- **UUID**: Generación de identificadores únicos

### Frontend:
- **React**: Biblioteca de JavaScript para UI
- **React Router**: Navegación entre páginas
- **Tailwind CSS**: Framework de CSS para estilos
- **Shadcn/UI**: Componentes de interfaz de usuario
- **Lucide React**: Iconos modernos
- **Vite**: Herramienta de construcción rápida

## 📁 Estructura del Proyecto

```
likeFriends/
├── src/
│   ├── models/
│   │   ├── user.py          # Modelo base de usuario
│   │   └── room.py          # Modelos de sala y participante
│   ├── routes/
│   │   ├── user.py          # Rutas de usuario (plantilla)
│   │   └── room.py          # Rutas de API para salas
│   ├── static/              # Archivos del frontend construido
│   ├── database/
│   │   └── app.db          # Base de datos SQLite
│   └── main.py             # Punto de entrada de la aplicación
├── venv/                   # Entorno virtual de Python
├── requirements.txt        # Dependencias de Python
└── README.md              # Este archivo
```

## 🔧 Instalación y Configuración para Windows

### Prerrequisitos:
- Python 3.8 o superior
- Node.js 16 o superior (solo para desarrollo del frontend)
- Git (opcional)

### Pasos de Instalación:

1. **Clonar o descargar el proyecto**
   ```bash
   # Si tienes Git instalado
   git clone <url-del-repositorio>
   cd likeFriends
   
   # O simplemente extrae el archivo ZIP descargado
   ```

2. **Crear y activar entorno virtual**
   ```bash
   # En Windows Command Prompt
   python -m venv venv
   venv\\Scripts\\activate
   
   # En Windows PowerShell
   python -m venv venv
   venv\\Scripts\\Activate.ps1
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**
   ```bash
   python src/main.py
   ```

5. **Acceder a la aplicación**
   - Abre tu navegador web
   - Ve a: `http://localhost:5001`

## 🎮 Cómo Usar la Aplicación

### Crear una Nueva Sala:
1. Ve a la página principal
2. Haz clic en "Crear Sala"
3. Ingresa un nombre para tu sala
4. Copia y comparte el enlace de invitación o código con tus amigos

### Unirse a una Sala:
1. Usa el enlace de invitación proporcionado por el administrador
2. O ingresa el código de invitación en la página principal
3. Escribe tu nombre y haz clic en "Unirse a la Sala"
4. Guarda tu enlace personal para ver tu amigo secreto

### Realizar el Sorteo (Solo Administrador):
1. Ve al panel de administración
2. Espera a que se unan al menos 2 participantes
3. Haz clic en "Realizar Sorteo"
4. ¡Todos los participantes ya pueden ver su amigo secreto!

## 🔧 Desarrollo y Personalización

### Modificar el Frontend:
1. Ve al directorio `likeFriends-frontend/`
2. Instala dependencias: `npm install` o `pnpm install`
3. Ejecuta el servidor de desarrollo: `npm run dev`
4. Realiza tus cambios en los archivos de `src/`
5. Construye para producción: `npm run build`
6. Copia los archivos de `dist/` a `likeFriends/src/static/`

### Modificar el Backend:
1. Edita los archivos en `src/models/` para cambiar la estructura de datos
2. Modifica `src/routes/room.py` para agregar nuevas funcionalidades de API
3. Actualiza `src/main.py` para configuraciones generales

### Base de Datos:
- La aplicación usa SQLite por defecto (archivo `src/database/app.db`)
- Para cambiar a otra base de datos, modifica la configuración en `src/main.py`

## 🚀 Despliegue en Producción

La aplicación ya está desplegada en: https://p9hwiqcq8w7x.manus.space

Para desplegar en tu propio servidor:

1. **Preparar para producción**:
   - Cambia `debug=False` en `src/main.py`
   - Configura variables de entorno para la base de datos
   - Usa un servidor WSGI como Gunicorn

2. **Ejemplo con Gunicorn**:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 src.main:app
   ```

## 🐛 Solución de Problemas

### Error de Puerto en Uso:
- Cambia el puerto en `src/main.py` línea 47
- O mata el proceso que usa el puerto 5001

### Error de Base de Datos:
- Elimina el archivo `src/database/app.db`
- Reinicia la aplicación para recrear la base de datos

### Error de CORS:
- Verifica que Flask-CORS esté instalado
- Asegúrate de que `CORS(app)` esté en `src/main.py`

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:
1. Haz fork del proyecto
2. Crea una rama para tu feature
3. Realiza tus cambios
4. Envía un pull request

## 📞 Soporte

Si tienes problemas o preguntas:
1. Revisa la sección de solución de problemas
2. Verifica que todas las dependencias estén instaladas
3. Asegúrate de estar usando Python 3.8 o superior

---

¡Disfruta organizando tus intercambios de regalos con likeFriends! 🎁

