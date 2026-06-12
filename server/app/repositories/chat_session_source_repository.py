from sqlalchemy.orm import Session

from app.models.chat_session_source import (
    ChatSessionSource
)


def attach_source_to_session(
    db: Session,
    session_id: int,
    source_id: int
):

    record = ChatSessionSource(
        session_id=session_id,
        source_id=source_id
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record


def get_source_ids_by_session(
    db: Session,
    session_id: int
):

    records = (
        db.query(ChatSessionSource)
        .filter(
            ChatSessionSource.session_id == session_id
        )
        .all()
    )

    return [
        record.source_id
        for record in records
    ]


def delete_sources_by_session(
    db: Session,
    session_id: int
):

    (
        db.query(ChatSessionSource)
        .filter(
            ChatSessionSource.session_id == session_id
        )
        .delete()
    )

    db.commit()


def delete_sessions_by_source(
    db: Session,
    source_id: int
):

    (
        db.query(ChatSessionSource)
        .filter(
            ChatSessionSource.source_id == source_id
        )
        .delete()
    )

    db.commit()
