from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey
)

from app.database.connection import Base


class Chunk(Base):

    __tablename__ = "chunks"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    source_id = Column(
        Integer,
        ForeignKey("sources.id"),
        nullable=False
    )

    chunk_index = Column(
        Integer
    )

    content = Column(
        Text
    )

    page = Column(
        Integer
    )