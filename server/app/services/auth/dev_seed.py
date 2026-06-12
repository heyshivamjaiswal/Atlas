from sqlalchemy.orm import Session

from app.models.user import User


def create_dev_user(db: Session):

    existing_user = (
        db.query(User)
        .filter(
            User.email == "dev@atlas.local"
        )
        .first()
    )

    if existing_user:
        return existing_user

    user = User(
        email="dev@atlas.local",
        password_hash="dev-password"
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    print(
        f"Created dev user: {user.id}"
    )

    return user
