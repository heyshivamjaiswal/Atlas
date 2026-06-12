from fastapi import HTTPException

from app.repositories.chat_session_repository import (
    create_chat_session,
    get_chat_session_by_id,
    get_chat_sessions,
    delete_chat_session
)

from app.repositories.message_repository import (
    get_messages_by_session,
    delete_messages_by_session
)


def create_session(
        db,
        user_id: int,
        title: str
):

    session = create_chat_session(
        db,
        user_id,
        title
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

    messages = get_messages_by_session(
        db,
        session_id
    )

    return {
        "id": session.id,
        "title": session.title,
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

    delete_chat_session(
        db,
        session
    )

    return {
        "message": "Chat deleted"
    }
