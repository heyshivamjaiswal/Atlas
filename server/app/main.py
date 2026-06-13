from fastapi import FastAPI
from contextlib import asynccontextmanager


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

from app.routes.chat import (
    router as chat_router
)

from app.services.vector.vector_health import (
    ensure_collection_exists
)

from app.core.exception_handlers import (
    register_exception_handlers
)

import app.models.chat_session
import app.models.message
import app.models.chat_session_source

from app.core.startup_checks import (
    validate_environment
)

# Create tables
Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):

    ensure_collection_exists()

    yield

validate_environment()

app = FastAPI(
    lifespan=lifespan
)

register_exception_handlers(
    app
)


@app.get("/")
def root():

    return {
        "message": "Atlas backend working"
    }


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

app.include_router(
    chat_router
)
