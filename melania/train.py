"""Simple training script using logged conversations."""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

DB_PATH = Path(__file__).resolve().parent / "conversations.db"


def load_data():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT mensaje_usuario, respuesta_melania FROM conversations")
    rows = c.fetchall()
    conn.close()
    texts = [row[0] for row in rows]
    labels = [row[1] for row in rows]
    return texts, labels


def train_model():
    texts, labels = load_data()
    if not texts:
        print("No conversations to train on")
        return
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", LogisticRegression()),
    ])
    pipeline.fit(texts, labels)
    print(f"Trained model on {len(texts)} conversations")


if __name__ == "__main__":
    train_model()
