import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

from fastapi.testclient import TestClient  # noqa: E402
from melania.main import app  # noqa: E402


client = TestClient(app)


def test_read_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "MELANO INC API Online"}


def test_chat_endpoint() -> None:
    payload = {"user_id": "test", "message": "hola"}
    response = client.post("/hermes/chat", json=payload)
    assert response.status_code == 200
    assert "respuesta" in response.json()
