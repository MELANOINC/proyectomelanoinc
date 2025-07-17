from fastapi import APIRouter
from pydantic import BaseModel
from pathlib import Path
import joblib
from ..conversations import log_conversation

MODEL_PATH = Path(__file__).resolve().parent.parent / "model.joblib"

try:
    MODEL = joblib.load(MODEL_PATH)
except FileNotFoundError:
    MODEL = None


class Message(BaseModel):
    user_id: str
    message: str


router = APIRouter()


@router.get("/")
def status() -> dict:
    return {"hermes": "online"}


@router.post("/chat")
def chat(message: Message) -> dict:
    """Simple chat endpoint that logs the conversation."""
    if MODEL:
        respuesta = MODEL.predict([message.message])[0]
    else:
        # Fallback response if no model is available
        respuesta = "Hola, soy Melania"
    log_conversation(
        user_id=message.user_id,
        mensaje_usuario=message.message,
        respuesta_melania=respuesta,
        etiquetas=[],
    )
    return {"respuesta": respuesta}
