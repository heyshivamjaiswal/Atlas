from app.database.connection import (
    engine,
    Base
)

import app.models.user
import app.models.source
import app.models.chunk


def create_tables():

    Base.metadata.create_all(
        bind=engine
    )


create_tables()