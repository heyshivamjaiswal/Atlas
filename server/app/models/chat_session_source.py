from sqlalchemy import (
    Column,
    Integer,
    ForeignKey
)

from app.database.connection import Base


class ChatSessionSource(Base):

    __tablename__ = "chat_session_sources"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    session_id = Column(
        Integer,
        ForeignKey("chat_sessions.id"),
        nullable=False
    )

    source_id = Column(
        Integer,
        ForeignKey("sources.id"),
        nullable=False
    )
