from sqlalchemy.orm import Session

from app.models.source import Source


def create_source(
    db: Session,
    user_id: int,
    source_type: str,
    title: str | None,
    file_name: str | None,
    storage_key: str | None = None
):

    source = Source(
        user_id=user_id,
        source_type=source_type,
        title=title,
        file_name=file_name,
        storage_key=storage_key
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


def delete_sources_by_user_id(
        db: Session,
        user_id: int
):

    (
        db.query(Source)
        .filter(
            Source.user_id == user_id
        )
        .delete()
    )

    db.commit()


def count_sources_by_type(
    db: Session,
    user_id: int,
    source_type: str
):

    return (
        db.query(Source)
        .filter(
            Source.user_id == user_id,
            Source.source_type == source_type
        )
        .count()
    )


def get_sources_paginated(
    db: Session,
    user_id: int,
    search: str | None,
    skip: int,
    limit: int
):

    query = (
        db.query(Source)
        .filter(
            Source.user_id == user_id
        )
    )

    if search:

        query = query.filter(
            Source.title.ilike(
                f"%{search}%"
            )
        )

    return (
        query
        .offset(skip)
        .limit(limit)
        .all()
    )
