from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def status() -> dict:
    return {"athena": "online"}
