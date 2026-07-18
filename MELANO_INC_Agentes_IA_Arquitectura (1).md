# MELANO INC – Documentación Técnica de Arquitectura con Agentes IA Interconectados

## 💠 Proyecto

**MELANO INC – Plataforma SaaS de Automatización Inteligente con Agentes IA Interconectados**

---

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "MELANO INC API Online"}fastapi
uvicorn
pytest
flake8name: Deploy MELANO INC

on:
  push:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest tests/

      - name: Lint code
        run: |
          flake8 .

      - name: Build Docker image
        run: |
          docker build -t ${{ secrets.DOCKERHUB_USERNAME }}/melano-inc:latest .

      - name: Login to DockerHub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Push Docker image
        run: |
          docker push ${{ secrets.DOCKERHUB_USERNAME }}/melano-inc:latest

      - name: Deploy to server
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SERVER_SSH_KEY }}
          script: |
            docker pull ${{ secrets.DOCKERHUB_USERNAME }}/melano-inc:latest
            docker stop melano-inc || true
            docker rm melano-inc || true
            docker run -d --name melano-inc -p 80:80 ${{ secrets.DOCKERHUB_USERNAME }}/melano-inc:latest

      - name: Notify Slack (via Chronos)
        run: |
          curl -X POST -H 'Content-type: application/json' --data '{"text":"🚀 MELANO INC desplegado correctamente."}' ${{ secrets.SLACK_WEBHOOK_URL }}## 1. 📐 ARQUITECTURA GENERAL

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

```yaml
name: Deploy MELANO INC

on:
  push:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest tests/

      - name: Lint code
        run: |
          flake8 .

      - name: Build Docker image
        run: |
          docker build -t ${{ secrets.DOCKERHUB_USERNAME }}/melano-inc:latest .

      - name: Login to DockerHub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Push Docker image
        run: |
          docker push ${{ secrets.DOCKERHUB_USERNAME }}/melano-inc:latest

      - name: Deploy to server
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SERVER_SSH_KEY }}
          script: |
            docker pull ${{ secrets.DOCKERHUB_USERNAME }}/melano-inc:latest
            docker stop melano-inc || true
            docker rm melano-inc || true
            docker run -d --name melano-inc -p 80:80 ${{ secrets.DOCKERHUB_USERNAME }}/melano-inc:latest

      - name: Notify Slack (via Chronos)
        run: |
          curl -X POST -H 'Content-type: application/json' --data '{"text":"🚀 MELANO INC desplegado correctamente."}' ${{ secrets.SLACK_WEBHOOK_URL }}
```

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "MELANO INC API Online"}

## 9. 📚 REQUISITOS

- fastapi
- uvicorn
- pytest
- flake8

## 10. 🐳 DOCKER

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "80"]
```

from fastapi.testclient import TestClient
from index import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "MELANO INC API Online"}

git init
git add .
git commit -m "Initial MELANO INC workspace with FastAPI, Docker, CI/CD and tests"
git remote add origin <https://github.com/TU_USUARIO/TU_REPO.git>
git branch -M main
git push -u origin main

docker-compose up --build
