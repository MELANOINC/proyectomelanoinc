import sqlite3
import json
from pathlib import Path
from typing import List

DB_PATH = Path(__file__).resolve().parent / "conversations.db"


def init_db() -> None:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            mensaje_usuario TEXT,
            respuesta_melania TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            etiquetas TEXT
        )
        """
    )
    conn.commit()
    conn.close()


def log_conversation(
    user_id: str,
    mensaje_usuario: str,
    respuesta_melania: str,
    etiquetas: List[str] | None = None,
) -> None:
    init_db()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO conversations (user_id, mensaje_usuario, respuesta_melania, etiquetas) VALUES (?, ?, ?, ?)",
        (user_id, mensaje_usuario, respuesta_melania, json.dumps(etiquetas or [])),
    )
    conn.commit()
    conn.close()
