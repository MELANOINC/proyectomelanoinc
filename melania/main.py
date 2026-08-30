from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .agents import hermes, ares, chronos, athena


app = FastAPI(title="MELANO INC")


# Mount static files for Vercel Analytics integration
static_dir = Path(__file__).parent / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


app.include_router(hermes.router, prefix="/hermes", tags=["hermes"])
app.include_router(ares.router, prefix="/ares", tags=["ares"])
app.include_router(chronos.router, prefix="/chronos", tags=["chronos"])
app.include_router(athena.router, prefix="/athena", tags=["athena"])


@app.get("/")
def read_root():
    """Serve the main landing page with Vercel Analytics."""
    index_path = Path(__file__).parent / "static" / "index.html"
    if index_path.exists():
        return FileResponse(index_path)
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
