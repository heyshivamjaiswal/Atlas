from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.dependencies import (
    get_db
)

from app.schemas.auth import (
    RegisterRequest,
    RegisterResponse
)

from app.services.auth.auth_service import (
    register_user
)

router = APIRouter(

    prefix="/auth",

    tags=["auth"]
)


@router.post(

    "/register",

    response_model=RegisterResponse
)
def register(

    data: RegisterRequest,

    db: Session = Depends(
        get_db
    )
):

    return register_user(

        db,

        data.email,

        data.password
    )