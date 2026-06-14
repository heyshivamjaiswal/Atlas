from sqlalchemy import text

from app.database.connection import engine

from app.services.vector.qdrant_connection import (
    client
)

from app.core.logger import logger


def get_system_health():

    postgres = "down"
    qdrant = "down"

    try:

        with engine.connect() as conn:

            conn.execute(
                text("SELECT 1")
            )

        postgres = "ok"

    except Exception as e:

        logger.error(
            f"Postgres health check failed : {e}"
        )

    try:

        client.get_collections()

        qdrant = "ok"

    except Exception as e:

        logger.error(
            f"Qdrant health check failed: {e}"
        )

    return {

        "api": "ok",

        "postgres": postgres,

        "qdrant": qdrant
    }
