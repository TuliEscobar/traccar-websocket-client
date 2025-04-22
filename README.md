# Cliente API Traccar

Este proyecto es un cliente API para Traccar que permite obtener información de dispositivos GPS en tiempo real, utilizando tanto REST API como WebSocket.

## Requisitos

- Python 3.8 o superior
- Servidor Traccar funcionando (por defecto en http://localhost:8082)

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd TRAKII-API
```

2. Crear un entorno virtual e instalar dependencias:
```bash
python -m venv venv
.\venv\Scripts\activate  # En Windows
pip install -r requirements.txt
```

3. Configurar variables de entorno:
Copiar el archivo `.env.example` a `.env` y modificar las variables según tu configuración.
Puedes usar autenticación por token O por usuario/contraseña:

```
TRACCAR_URL=http://localhost:8082

# Opción 1: Autenticación por token (recomendada)
TRACCAR_TOKEN=tu_token_de_acceso

# Opción 2: Autenticación por usuario/contraseña
TRACCAR_USER=tu_usuario
TRACCAR_PASSWORD=tu_contraseña
```

Para obtener un token de acceso, puedes generarlo desde la interfaz web de Traccar o mediante una llamada a la API.

## Uso

1. Iniciar el servidor:
```bash
python main.py
```

2. Acceder a las interfaces disponibles:
   - Cliente Web con WebSocket: http://localhost:8000
   - API REST: http://localhost:8000/docs

## Funcionalidades

### Cliente Web con WebSocket
La página principal (http://localhost:8000) proporciona:
- Conexión WebSocket en tiempo real con Traccar
- Visualización del estado de la conexión
- Visualización de actualizaciones en tiempo real de:
  - Dispositivos
  - Posiciones
  - Eventos

### Endpoints REST API

- `GET /devices`: Obtiene lista de todos los dispositivos
- `GET /positions`: Obtiene las posiciones actuales de todos los dispositivos
- `GET /devices/{device_id}/positions`: Obtiene las posiciones de un dispositivo específico

## Formato de Mensajes WebSocket

Los mensajes recibidos a través del WebSocket tienen el siguiente formato:

```json
{
  "devices": [...],    // Actualizaciones de dispositivos
  "positions": [...],  // Actualizaciones de posiciones
  "events": [...]     // Eventos del sistema
}
```

## Documentación

- **API REST**: 
  - Swagger UI: http://localhost:8000/docs
  - ReDoc: http://localhost:8000/redoc

- **Documentación de Traccar**:
  - [API Reference](https://www.traccar.org/api-reference/)
  - [WebSocket API](https://www.traccar.org/traccar-api/)

## Desarrollo

### Estructura del Proyecto
```
TRAKII-API/
├── main.py              # Servidor FastAPI principal
├── requirements.txt     # Dependencias del proyecto
├── .env                # Configuración y credenciales
└── templates/
    └── index.html      # Cliente WebSocket
```

### Dependencias Principales
- FastAPI: Framework web moderno y rápido
- Uvicorn: Servidor ASGI para Python
- Requests: Cliente HTTP para Python
- Jinja2: Motor de plantillas
- python-dotenv: Manejo de variables de entorno 