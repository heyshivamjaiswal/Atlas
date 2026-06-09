import hashlib

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

    password_hash = hashlib.sha256(

        password.encode()

    ).hexdigest()

    return create_user(

        db,

        email,

        password_hash
    )