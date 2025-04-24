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

## 🚀 Instalación y Uso

### Opción 1: Usando Docker Compose (Recomendado)

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/TuliEscobar/traccar-websocket-client.git
   cd traccar-websocket-client
   ```

2. **Configurar variables de entorno:**
   ```bash
   cp .env.example .env
   ```
   Edita el archivo `.env` con las siguientes variables:
   ```env
   # Variables requeridas
   SECRET_KEY=tu_clave_secreta_aqui
   POSTGRES_PASSWORD=tu_contraseña_postgres_aqui

   # Variables opcionales (valores por defecto)
   POSTGRES_USER=gpsuser
   POSTGRES_DB=gpsdb
   DATABASE_URL=postgresql://gpsuser:gpspass@db:5432/gpsdb
   TRACCAR_API_URL=http://traccar:8082
   REDIS_URL=redis://redis:6379/0
   ```

3. **Iniciar los servicios:**
   ```bash
   docker compose up -d
   ```

4. **Verificar que los servicios estén funcionando:**
   ```bash
   docker compose ps
   ```

Los servicios estarán disponibles en:
- Traccar: http://localhost:5055 (datos GPS)
- API: http://localhost:8000
- Interfaz Web: http://localhost

### Variables de Entorno Detalladas

```env
# Variables Requeridas
SECRET_KEY=tu_clave_secreta_aqui          # Clave para encriptación y tokens
POSTGRES_PASSWORD=tu_contraseña_postgres_aqui      # Contraseña de PostgreSQL

# Variables Opcionales
POSTGRES_USER=gpsuser                     # Usuario de PostgreSQL (default: gpsuser)
POSTGRES_DB=gpsdb                         # Nombre de la base de datos (default: gpsdb)
DATABASE_URL=postgresql://gpsuser:gpspass@db:5432/gpsdb  # URL de conexión a PostgreSQL
TRACCAR_API_URL=http://traccar:8082       # URL interna de Traccar
REDIS_URL=redis://redis:6379/0            # URL de conexión a Redis
```

### Opción 2: Instalación Local

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

## 🐳 Servicios Docker

El proyecto utiliza Docker Compose para orquestar los siguientes servicios:

### Traccar
- Puerto: 5055 (TCP/UDP para datos GPS)
- Almacenamiento persistente para datos y logs
- Monitoreo de salud cada 30 segundos

### API
- Puerto: 8000
- Conexión con base de datos PostgreSQL y Redis
- Variables de entorno configurables
- Monitoreo de salud del endpoint `/health`

### Base de Datos (PostgreSQL)
- Puerto: 5432
- Almacenamiento persistente
- Variables de entorno configurables para usuario y contraseña
- Monitoreo de salud con `pg_isready`

### Redis
- Puerto: 6379
- Almacenamiento persistente
- Monitoreo de salud con ping

### Nginx
- Puertos: 80 (HTTP) y 443 (HTTPS)
- Proxy inverso para la API
- Soporte para SSL/TLS
- Monitoreo de salud de la configuración

## 🔍 Diagnóstico

### Verificación de Servicios Docker
```bash
# Ver estado de todos los servicios
docker compose ps

# Ver logs de un servicio específico
docker compose logs [servicio]

# Ver logs en tiempo real
docker compose logs -f [servicio]

# Reiniciar un servicio
docker compose restart [servicio]
```

### Interfaz Web
La interfaz incluye una sección de diagnóstico que muestra:
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

## 📝 Configuración de Traccar

### Acceso a la Interfaz Web
1. Una vez que los contenedores estén en ejecución, accede a:
   - URL: `http://localhost:8082`
   - Usuario: `admin`
   - Contraseña: `admin`

### Pasos de Configuración

1. **Cambiar Contraseña de Administrador**
   - Ve a Configuración > Usuario
   - Cambia la contraseña por defecto
   - Guarda los cambios

2. **Configurar Servidor**
   - El servidor escucha conexiones GPS en el puerto 5055
   - Protocolo por defecto: TCP
   - Los dispositivos deben configurarse para conectarse a: `tu-ip-servidor:5055`

3. **Agregar un Dispositivo**
   - Ve a Dispositivos > Añadir (+)
   - Campos requeridos:
     * Nombre: Identificador amigable
     * Identificador: IMEI o ID único del dispositivo
   - Campos opcionales:
     * Teléfono
     * Modelo
     * Categoría

4. **Verificar Conexión**
   - El dispositivo aparecerá en la lista principal
   - Estados posibles:
     * 🟢 Verde: Conectado y reportando
     * 🔴 Rojo: Desconectado
     * ⚪ Gris: Sin datos recientes

### Solución de Problemas

1. **Si el dispositivo no conecta:**
   - Verifica que el puerto 5055 esté accesible
   - Confirma que el IMEI/ID sea correcto
   - Revisa los logs en `traccar/logs/tracker-server.log`

2. **Si no ves datos:**
   - Verifica la conexión del dispositivo GPS
   - Confirma que tenga señal GPS
   - Revisa el intervalo de actualización configurado