from sqlalchemy import text

from app.database.connection import engine

from app.services.vector.qdrant_connection import (
    client
)


def get_system_health():

    postgres = "down"
    qdrant = "down"

    try:

        with engine.connect() as conn:

            conn.execute(
                text("SELECT 1")
            )

        postgres = "ok"

    except Exception:

        pass

    try:

        client.get_collections()

        qdrant = "ok"

    except Exception:

        pass

    return {

        "api": "ok",

        "postgres": postgres,

        "qdrant": qdrant
    }
