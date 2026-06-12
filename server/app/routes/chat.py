from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.dependencies import (
    get_db
)

from app.services.auth.current_user import (
    get_current_user
)

from app.schemas.chat import (
    CreateChatRequest
)

from app.services.chat.chat_service import (
    create_session,
    list_sessions,
    get_session_history,
    delete_session
)

router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)


@router.post("")
def create_chat(

    data: CreateChatRequest,

    db: Session = Depends(
        get_db
    ),

    current_user=Depends(
        get_current_user
    )
):

    return create_session(

        db,

        current_user.id,

        data.title,

        data.source_ids
    )


@router.get("")
def get_chats(

    db: Session = Depends(
        get_db
    ),

    current_user=Depends(
        get_current_user
    )
):

    return list_sessions(

        db,

        current_user.id
    )


@router.get("/{session_id}")
def get_chat(

    session_id: int,

    db: Session = Depends(
        get_db
    ),

    current_user=Depends(
        get_current_user
    )
):

    return get_session_history(

        db,

        session_id,

        current_user.id
    )


@router.delete("/{session_id}")
def delete_chat(

    session_id: int,

    db: Session = Depends(
        get_db
    ),

    current_user=Depends(
        get_current_user
    )
):

    return delete_session(

        db,

        session_id,

        current_user.id
    )
