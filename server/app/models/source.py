from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from app.database.connection import Base


class Source(Base):

    __tablename__ = "sources"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    source_type = Column(
        String,
        nullable=False
    )

    title = Column(
        String
    )

    file_name = Column(
        String
    )

    storage_key = Column(
        String(500),
        nullable=True
    )
