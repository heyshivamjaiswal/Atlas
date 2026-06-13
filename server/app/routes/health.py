from fastapi import APIRouter

from app.services.system.health_service import (
    get_system_health
)

router = APIRouter(
    prefix="/system",
    tags=["system"]
)


@router.get("/health")
def health():

    return get_system_health()


@router.get("/version")
def version():

    return {

        "backend": "atlas",

        "version": "0.1"
    }
