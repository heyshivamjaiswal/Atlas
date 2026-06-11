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
    RegisterResponse,
    LoginRequest,
    LoginResponse
)

from app.services.auth.auth_service import (
    register_user,
    login_user
)

from app.services.auth.current_user import (
    get_current_user
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
    db: Session = Depends(get_db)
):

    return register_user(
        db,
        data.email,
        data.password
    )


@router.post(
    "/login",
    response_model=LoginResponse
)
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):

    return login_user(
        db,
        data.email,
        data.password
    )


@router.get("/me")
def me(
    current_user=Depends(
        get_current_user
    )
):

    return {
        "id": current_user.id,
        "email": current_user.email
    }
