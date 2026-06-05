from fastapi import FastAPI

from app.routes.health import router as health_router
from app.routes.source import router as source_router
from app.routes.query import router as query_router

app = FastAPI()

@app.get("/")
def root():
    return{
        "message": "Atlas backend working"
    }

app.include_router(health_router)

app.include_router(source_router)

app.include_router(query_router)