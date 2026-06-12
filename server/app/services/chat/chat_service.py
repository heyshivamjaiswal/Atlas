from fastapi import HTTPException

from app.repositories.chat_session_repository import (
    create_chat_session,
    get_chat_sessions,
    get_chat_session_by_id,
    delete_chat_session
)

from app.repositories.message_repository import (
    get_messages_by_session,
    delete_messages_by_session
)

from app.repositories.chat_session_source_repository import (
    attach_source_to_session,
    get_source_ids_by_session,
    delete_sources_by_session
)

from app.repositories.source_repository import (
    get_source_by_id_and_user
)


def create_session(
    db,
    user_id: int,
    title: str,
    source_ids: list[int]
):

    session = create_chat_session(
        db,
        user_id,
        title
    )

    for source_id in source_ids:

        source = get_source_by_id_and_user(
            db,
            source_id,
            user_id
        )

        if not source:

            raise HTTPException(
                status_code=404,
                detail=f"Source {source_id} not found"
            )

        attach_source_to_session(
            db,
            session.id,
            source_id
        )

    return {
        "id": session.id,
        "title": session.title
    }


def list_sessions(
    db,
    user_id: int
):

    sessions = get_chat_sessions(
        db,
        user_id
    )

    return [
        {
            "id": session.id,
            "title": session.title,
            "created_at": session.created_at
        }
        for session in sessions
    ]


def get_session_history(
    db,
    session_id: int,
    user_id: int
):

    session = get_chat_session_by_id(
        db,
        session_id,
        user_id
    )

    if not session:

        raise HTTPException(
            status_code=404,
            detail="Chat session not found"
        )

    source_ids = get_source_ids_by_session(
        db,
        session_id
    )

    messages = get_messages_by_session(
        db,
        session_id
    )

    return {
        "id": session.id,
        "title": session.title,
        "source_ids": source_ids,
        "messages": [
            {
                "role": message.role,
                "content": message.content
            }
            for message in messages
        ]
    }


def delete_session(
    db,
    session_id: int,
    user_id: int
):

    session = get_chat_session_by_id(
        db,
        session_id,
        user_id
    )

    if not session:

        raise HTTPException(
            status_code=404,
            detail="Chat session not found"
        )

    delete_messages_by_session(
        db,
        session_id
    )

    delete_sources_by_session(
        db,
        session_id
    )

    delete_chat_session(
        db,
        session
    )

    return {
        "message": "Chat deleted"
    }
