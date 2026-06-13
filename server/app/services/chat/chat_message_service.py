from fastapi import HTTPException

from app.repositories.chat_session_repository import (
    get_chat_session_by_id
)

from app.repositories.chat_session_source_repository import (
    get_source_ids_by_session
)

from app.services.llm.rag_service import (
    answer_query
)

from app.repositories.message_repository import (
    create_message,
    get_messages_by_session
)


def send_message(

    db,

    session_id: int,

    user_id: int,

    message: str
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

    recent_messages = messages[-10:]

    conversation_history = "\n".join(
        [
            f"{message.role.capitalize()}: {message.content}"
            for message in recent_messages
        ]
    )

   # save current user message
    create_message(

        db,

        session_id,

        "user",

        message
    )

    result = answer_query(

        query=message,

        db=db,

        user_id=user_id,

        source_ids=source_ids,

        conversation_history=conversation_history
    )

    create_message(

        db,

        session_id,

        "assistant",

        result["answer"]
    )

    return result
