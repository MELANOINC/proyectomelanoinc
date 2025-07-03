from fastapi import APIRouter
from pydantic import BaseModel
from ..conversations import log_conversation


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
    # Placeholder response generation
    respuesta = "Hola, soy Melania"
    log_conversation(
        user_id=message.user_id,
        mensaje_usuario=message.message,
        respuesta_melania=respuesta,
        etiquetas=[],
    )
    return {"respuesta": respuesta}
