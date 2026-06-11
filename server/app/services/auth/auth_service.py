from app.services.auth.password_service import (
    hash_password
)

from app.services.auth.password_service import (
    hash_password,
    verify_password
)

from app.services.auth.jwt_service import (
    create_access_token
)

from sqlalchemy.orm import Session

from fastapi import HTTPException

from app.repositories.user_repository import (
    get_user_by_email,
    create_user
)


def register_user(
    db: Session,
    email: str,
    password: str
):

    existing = get_user_by_email(
        db,
        email
    )

    if existing:

        raise HTTPException(

            status_code=400,

            detail="User already exists"
        )

    password_hash = hash_password(password)

    return create_user(

        db,

        email,

        password_hash
    )


def login_user(
    db: Session,
    email: str,
    password: str
):

    user = get_user_by_email(
        db,
        email
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        password,
        user.password_hash
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        user.id
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
