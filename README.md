# proyectomelanoinc

MELANO INC – Documentación Técnica de Arquitectura con Agentes IA Interconectados

## 💠 Proyecto:
**MELANO INC – Plataforma SaaS de Automatización Inteligente con Agentes IA Interconectados**

---

## 1. 📐 ARQUITECTURA GENERAL

### 🔷 Diagrama de Capas

```
[Cliente/Usuario Final]
        │
        ▼
[Agent Hermes] ─ Leads y Ventas
        │
        ├──► [Agent Ares] ─ Bots de Inversión (Scalping / Arbitraje / Tendencias)
        │
        ├──► [Agent Chronos] ─ Automatización de Flujo (Onboarding, Activaciones)
        │
        └──► [Agent Athena] ─ Analítica y Rendimiento
        │
        ▼
[Melania OS] ─ Orquestadora Central (Lógica, IA, Seguridad, APIs)
        │
        ▼
[Infraestructura Cloud + Base de Datos + Logging Centralizado]
```

...

## 8. 📦 DEPLOYMENT PIPELINE

- CI/CD: GitHub Actions + Docker Build
- Auto-deploy si tests y linters pasan
- Notificaciones en Slack vía Agent Chronos


## 🚀 Quickstart

```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn melania.main:app --reload

# Run tests
pytest
```

## 🛰️ Estado del ecosistema

El endpoint `GET /status` devuelve el estado de todos los agentes conectados.

## 📚 Conversaciones y entrenamiento

El endpoint `POST /hermes/chat` almacena cada mensaje y la respuesta generada en
una base de datos SQLite en `melania/conversations.db`. El script
`melania/train.py` carga esas conversaciones para entrenar un modelo de ejemplo
con `scikit-learn`.

```bash
python -m melania.train
```
