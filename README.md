# Cliente WebSocket Traccar 🛰️

Cliente WebSocket para Traccar que proporciona una interfaz web en tiempo real para monitorear dispositivos GPS, posiciones y eventos.

## 🌟 Características

- 📱 Interfaz web moderna y responsive
- 🔄 Conexión WebSocket en tiempo real con reconexión automática
- 📍 Visualización de:
  - Dispositivos activos
  - Posiciones en tiempo real
  - Eventos del sistema
- 🛡️ Manejo robusto de errores y diagnósticos
- 🔐 Soporte para autenticación por token

## 🛠️ Requisitos Previos

- Python 3.8 o superior
- Servidor Traccar configurado y funcionando
- Acceso a la API de Traccar (URL y credenciales)

## 📦 Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/TuliEscobar/traccar-websocket-client.git
   cd traccar-websocket-client
   ```

2. **Crear y activar entorno virtual (recomendado):**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno:**
   ```bash
   cp .env.example .env
   ```
   Edita el archivo `.env` con tus credenciales:
   ```env
   TRACCAR_URL=http://tu-servidor-traccar:8082
   TRACCAR_USER=tu-usuario
   TRACCAR_PASSWORD=tu-contraseña
   TRACCAR_TOKEN=tu-token  # Opcional, si prefieres usar token
   ```

## 🚀 Uso

1. **Iniciar el servidor:**
   ```bash
   python main.py
   ```
   El servidor estará disponible en `http://localhost:8000`

2. **Acceder a la interfaz web:**
   - Abre tu navegador y visita `http://localhost:8000`
   - La interfaz mostrará el estado de la conexión y los mensajes en tiempo real

## 🔌 API Endpoints

### Página Principal
- `GET /`
  - Interfaz web del cliente WebSocket
  - Requiere token configurado

### Dispositivos
- `GET /devices`
  - Lista todos los dispositivos
  - Respuesta: `List[Dict]`

### Posiciones
- `GET /positions`
  - Obtiene las posiciones actuales de todos los dispositivos
  - Respuesta: `List[Dict]`

### Posiciones por Dispositivo
- `GET /devices/{device_id}/positions`
  - Obtiene las posiciones de un dispositivo específico
  - Parámetros:
    - `device_id`: ID del dispositivo (int)
  - Respuesta: `List[Dict]`

## 🔍 Diagnóstico

La interfaz web incluye una sección de diagnóstico que muestra:
- Estado de la conexión WebSocket
- URL del WebSocket
- Estado del token
- Registro de eventos y errores

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🐛 Reporte de Problemas

Si encuentras algún problema o tienes una sugerencia:
1. Revisa que no exista un issue similar
2. Abre un nuevo issue con:
   - Descripción clara del problema
   - Pasos para reproducirlo
   - Comportamiento esperado
   - Capturas de pantalla (si aplica)

## 📞 Soporte

Para soporte y consultas:
- Abre un issue en GitHub
- Envía un correo a [tuliescobar@gmail.com]