import os
import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Dict, List
from pathlib import Path

# Cargar variables de entorno
load_dotenv()

# Configurar FastAPI y templates
app = FastAPI(title="Traccar API Client")
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Configuración de Traccar
TRACCAR_URL = os.getenv("TRACCAR_URL")
TRACCAR_USER = os.getenv("TRACCAR_USER")
TRACCAR_PASSWORD = os.getenv("TRACCAR_PASSWORD")
TRACCAR_TOKEN = os.getenv("TRACCAR_TOKEN", "").strip()

def get_traccar_session() -> requests.Session:
    """Crear una sesión autenticada con Traccar"""
    session = requests.Session()
    
    # Si hay un token disponible, usarlo
    if TRACCAR_TOKEN:
        session.get(f"{TRACCAR_URL}/api/session", params={"token": TRACCAR_TOKEN})
        return session
    
    # Si no hay token, usar autenticación por usuario/contraseña
    response = session.post(
        f"{TRACCAR_URL}/api/session",
        json={
            "email": TRACCAR_USER,
            "password": TRACCAR_PASSWORD
        }
    )
    if response.status_code != 200:
        raise HTTPException(status_code=401, detail="Error de autenticación con Traccar")
    return session

@app.get("/", response_class=HTMLResponse)
async def websocket_page(request: Request):
    """Página principal con cliente WebSocket"""
    if not TRACCAR_TOKEN:
        raise HTTPException(
            status_code=400,
            detail="No se ha configurado el token de Traccar en las variables de entorno"
        )
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "token": TRACCAR_TOKEN
        }
    )

@app.get("/devices", response_model=List[Dict])
async def get_devices():
    """Obtener lista de dispositivos"""
    try:
        session = get_traccar_session()
        response = session.get(f"{TRACCAR_URL}/api/devices")
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/positions", response_model=List[Dict])
async def get_positions():
    """Obtener posiciones actuales de todos los dispositivos"""
    try:
        session = get_traccar_session()
        response = session.get(f"{TRACCAR_URL}/api/positions")
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/devices/{device_id}/positions", response_model=List[Dict])
async def get_device_positions(device_id: int):
    """Obtener posiciones de un dispositivo específico"""
    try:
        session = get_traccar_session()
        response = session.get(f"{TRACCAR_URL}/api/positions?deviceId={device_id}")
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 