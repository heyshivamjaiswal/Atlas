from sqlalchemy.orm import Session

from app.models.source import Source


def create_source(
    db: Session,
    user_id: int,
    source_type: str,
    title: str | None,
    file_name: str | None
):

    source = Source(
        user_id=user_id,
        type=source_type,
        title=title,
        file_name=file_name
    )

    db.add(source)
    db.commit()
    db.refresh(source)

    return source


def get_sources(
    db: Session,
    user_id: int
):
    return (
        db.query(Source)
        .filter(
            Source.user_id == user_id
        )
        .all()
    )


def get_source_by_id_and_user(
    db: Session,
    source_id: int,
    user_id: int
):
    return (
        db.query(Source)
        .filter(
            Source.id == source_id,
            Source.user_id == user_id
        )
        .first()
    )


def delete_source(
    db: Session,
    source: Source
):
    db.delete(source)
    db.commit()


def get_source_ids_by_user(
    db: Session,
    user_id: int
):

    sources = (
        db.query(Source.id)
        .filter(
            Source.user_id == user_id
        )
        .all()
    )

    return [
        source.id
        for source in sources
    ]
