# Chat Bot Local

Este proyecto contiene una página web simple y un servidor local para ejecutar un chatbot que usa la API de OpenAI o un servidor compatible local.

## Archivos principales

- `chat.html`: Interfaz de usuario para el chat.
- `server.py`: Servidor HTTP local que sirve `chat.html` y reenvía las solicitudes de chat a la API.
- `main.py`: Ejemplo previo de uso directo de la librería `openai`.

## Requisitos

- Python 3.10+ (o compatible)
- Entorno virtual creado en `env/`
- Librería `openai` instalada en el entorno virtual

## Ejecución

1. Abre PowerShell en la carpeta del proyecto:
   ```powershell
   cd F:\CAPACITACION\PORTAFOLIO\IA-Agent
   ```

2. Activa el entorno virtual:
   ```powershell
   .\env\Scripts\Activate.ps1
   ```

3. Ejecuta el servidor local:
   ```powershell
   python .\server.py
   ```

4. Abre en el navegador:
   ```text
   http://localhost:8000/chat.html
   ```

## Configuración opcional

Puedes establecer variables de entorno antes de iniciar `server.py`:

- `OPENAI_API_BASE`: URL base de la API. Por defecto `http://localhost:11434/v1`
- `OPENAI_API_KEY`: Clave API. Por defecto `ollama`
- `CHAT_MODEL`: Modelo de chat. Por defecto `qwen3.5:397b-cloud`

Por ejemplo en PowerShell:
```powershell
$env:OPENAI_API_BASE = 'http://localhost:11434/v1'
$env:OPENAI_API_KEY = 'ollama'
$env:CHAT_MODEL = 'qwen3.5:397b-cloud'
python .\server.py
```

## Notas

- Si tu servidor local de OpenAI usa HTTPS, ajusta `OPENAI_API_BASE` con `https://...`.
- Si el servidor local no corre en el puerto `11434`, cambia el valor en `OPENAI_API_BASE`.
- `server.py` ya sirve la página desde la carpeta del proyecto y maneja la ruta `POST /api/chat`.
