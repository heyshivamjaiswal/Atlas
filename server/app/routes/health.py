from fastapi import APIRouter

router = APIRouter(
    prefix="/system",
    tags=["system"]
)

@router.get("/health")
def health():
    return{
        "status": "healthy"
    }

@router.get("/version")
def version():
    return{
        "backend": "atlas",
        "version": "0.1"
    }