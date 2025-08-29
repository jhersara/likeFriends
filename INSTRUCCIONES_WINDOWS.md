# 🪟 Instrucciones para Windows - likeFriends

## 📋 Requisitos del Sistema

- **Sistema Operativo**: Windows 10 o superior
- **Python**: Versión 3.8 o superior
- **Memoria RAM**: Mínimo 4GB recomendado
- **Espacio en Disco**: 500MB libres
- **Navegador Web**: Chrome, Firefox, Edge o Safari

## 🔧 Instalación Paso a Paso

### 1. Verificar Python
Abre **Command Prompt** (cmd) o **PowerShell** y ejecuta:
```cmd
python --version
```
Si no tienes Python instalado, descárgalo desde: https://python.org/downloads/

### 2. Extraer el Proyecto
1. Extrae el archivo ZIP descargado en una carpeta de tu elección
2. Ejemplo: `C:\Users\TuUsuario\Desktop\likeFriends\`

### 3. Abrir Terminal en la Carpeta del Proyecto
**Opción A - Command Prompt:**
1. Presiona `Win + R`
2. Escribe `cmd` y presiona Enter
3. Navega a la carpeta: `cd C:\ruta\a\tu\carpeta\likeFriends`

**Opción B - PowerShell:**
1. Presiona `Win + X` y selecciona "Windows PowerShell"
2. Navega a la carpeta: `cd C:\ruta\a\tu\carpeta\likeFriends`

**Opción C - Explorador de Archivos:**
1. Abre la carpeta del proyecto en el Explorador
2. Haz clic en la barra de direcciones
3. Escribe `cmd` y presiona Enter

### 4. Crear Entorno Virtual
```cmd
python -m venv venv
```

### 5. Activar Entorno Virtual

**En Command Prompt:**
```cmd
venv\Scripts\activate
```

**En PowerShell:**
```powershell
venv\Scripts\Activate.ps1
```

*Nota: Si tienes error en PowerShell, ejecuta primero:*
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 6. Instalar Dependencias
```cmd
pip install -r requirements.txt
```

### 7. Ejecutar la Aplicación
```cmd
python src/main.py
```

### 8. Abrir en el Navegador
1. Abre tu navegador web favorito
2. Ve a la dirección: `http://localhost:5001`
3. ¡Ya puedes usar likeFriends!

## 🚀 Ejecución Rápida (Próximas Veces)

Una vez instalado, para ejecutar la aplicación:

1. Abre terminal en la carpeta del proyecto
2. Activa el entorno virtual:
   ```cmd
   venv\Scripts\activate
   ```
3. Ejecuta la aplicación:
   ```cmd
   python src/main.py
   ```
4. Ve a `http://localhost:5001` en tu navegador

## 🛠️ Crear Acceso Directo (Opcional)

### Archivo Batch para Ejecución Rápida:
1. Crea un archivo llamado `ejecutar_likeFriends.bat` en la carpeta del proyecto
2. Agrega el siguiente contenido:
```batch
@echo off
cd /d "%~dp0"
call venv\Scripts\activate
python src/main.py
pause
```
3. Guarda el archivo
4. Haz doble clic en el archivo para ejecutar la aplicación

### Crear Acceso Directo en el Escritorio:
1. Haz clic derecho en `ejecutar_likeFriends.bat`
2. Selecciona "Crear acceso directo"
3. Arrastra el acceso directo al escritorio
4. Renómbralo como "likeFriends"

## 🔧 Configuración del Firewall de Windows

Si otros dispositivos en tu red no pueden acceder a la aplicación:

1. Abre "Windows Defender Firewall"
2. Haz clic en "Permitir una aplicación o característica a través de Windows Defender Firewall"
3. Haz clic en "Cambiar configuración"
4. Busca "Python" en la lista y asegúrate de que esté marcado para "Privada" y "Pública"
5. Si no aparece, haz clic en "Permitir otra aplicación..." y busca python.exe

## 🌐 Acceso desde Otros Dispositivos en la Red

Para que otros dispositivos (móviles, tablets, otras computadoras) accedan a tu aplicación:

1. **Encuentra tu IP local:**
   ```cmd
   ipconfig
   ```
   Busca la "Dirección IPv4" (ejemplo: 192.168.1.100)

2. **Modifica el archivo main.py:**
   - Abre `src/main.py` con un editor de texto
   - En la línea 48, cambia `debug=False` por `debug=True` si quieres ver logs
   - La aplicación ya está configurada para escuchar en todas las interfaces (0.0.0.0)

3. **Accede desde otros dispositivos:**
   - En otros dispositivos, ve a: `http://TU_IP_LOCAL:5001`
   - Ejemplo: `http://192.168.1.100:5001`

## 🐛 Solución de Problemas Comunes

### Error: "python no se reconoce como comando"
**Solución**: Instala Python desde python.org y asegúrate de marcar "Add Python to PATH" durante la instalación.

### Error: "No se puede ejecutar scripts en este sistema"
**Solución**: En PowerShell como administrador, ejecuta:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
```

### Error: "Puerto 5001 en uso"
**Solución**: 
1. Cierra otras aplicaciones que puedan usar el puerto
2. O cambia el puerto en `src/main.py` línea 47 (ejemplo: port=5002)

### Error: "ModuleNotFoundError"
**Solución**: 
1. Asegúrate de que el entorno virtual esté activado
2. Reinstala las dependencias: `pip install -r requirements.txt`

### La aplicación se cierra inmediatamente
**Solución**: 
1. Ejecuta desde Command Prompt/PowerShell para ver errores
2. Verifica que estés en la carpeta correcta del proyecto
3. Asegúrate de que el entorno virtual esté activado

### No puedo acceder desde otros dispositivos
**Solución**:
1. Verifica la configuración del firewall
2. Asegúrate de que todos los dispositivos estén en la misma red WiFi
3. Usa la IP correcta (no 127.0.0.1 o localhost)

## 📱 Uso en Dispositivos Móviles

La aplicación es completamente responsiva y funciona perfectamente en:
- **Android**: Chrome, Firefox, Samsung Internet
- **iOS**: Safari, Chrome
- **Tablets**: Cualquier navegador moderno

Simplemente accede a la URL desde el navegador móvil.

## 💡 Consejos de Uso

1. **Para grupos grandes**: La aplicación maneja sin problemas hasta 100+ participantes
2. **Backup de datos**: La base de datos se guarda en `src/database/app.db`
3. **Múltiples salas**: Puedes crear tantas salas como necesites
4. **Códigos únicos**: Cada sala tiene códigos únicos que no se repiten

## 🔄 Actualización de la Aplicación

Para actualizar a una nueva versión:
1. Haz backup de tu carpeta actual
2. Extrae la nueva versión en una carpeta diferente
3. Copia el archivo `src/database/app.db` de la versión anterior (si quieres conservar datos)
4. Sigue los pasos de instalación normalmente

---

¡Disfruta usando likeFriends en Windows! 🎁✨

