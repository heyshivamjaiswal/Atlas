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
        user_id = user_id,
        type = source_type,

        title = title,

        file_name = file_name
    )

    db.add(source)
    db.commit()
    db.refresh(source)
    
    return source