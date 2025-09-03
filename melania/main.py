from fastapi import FastAPI
from .agents import hermes, ares, chronos, athena


app = FastAPI(title="MELANO INC")


app.include_router(hermes.router, prefix="/hermes", tags=["hermes"])
app.include_router(ares.router, prefix="/ares", tags=["ares"])
app.include_router(chronos.router, prefix="/chronos", tags=["chronos"])
app.include_router(athena.router, prefix="/athena", tags=["athena"])


@app.get("/")
def read_root() -> dict:
    return {"message": "MELANO INC API Online"}


@app.get("/status")
def system_status() -> dict:
    """Return the availability of all agents."""
    return {
        "hermes": hermes.status()["hermes"],
        "ares": ares.status()["ares"],
        "chronos": chronos.status()["chronos"],
        "athena": athena.status()["athena"],
    }
