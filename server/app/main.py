from fastapi import FastAPI

import app.models.user
import app.models.source
import app.models.chunk

from app.database.connection import (
    Base,
    engine
)

from app.routes.health import router as health_router
from app.routes.source import router as source_router
from app.routes.query import router as query_router
from app.routes.auth import router as auth_router


# Create tables
Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
def root():

    return {
        "message": "Atlas backend working"
    }


app.include_router(
    health_router
)

app.include_router(
    source_router
)

app.include_router(
    query_router
)

app.include_router(
    auth_router
)
