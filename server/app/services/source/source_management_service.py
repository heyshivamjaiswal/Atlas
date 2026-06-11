from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.source_repository import (
    get_sources,
    get_source_by_id,
    delete_source as delete_source_record
)

from app.repositories.chunk_repository import (
    count_chunks_by_source_id,
    delete_chunks_by_source_id
)

from app.repositories.vector_repository import (
    delete_vectors_by_source_id
)


def list_sources(
    db: Session
):

    sources = get_sources(db)

    result = []

    for source in sources:

        result.append({

            "id": source.id,

            "type": source.type,

            "title": source.title,

            "chunk_count":
            count_chunks_by_source_id(
                db,
                source.id
            )
        })

    return result


def get_source_details(
    db: Session,
    source_id: int
):

    source = get_source_by_id(
        db,
        source_id
    )

    if not source:

        raise HTTPException(
            status_code=404,
            detail="Source not found"
        )

    return {

        "id": source.id,

        "type": source.type,

        "title": source.title,

        "file_name": source.file_name,

        "chunk_count":
        count_chunks_by_source_id(
            db,
            source.id
        )
    }


def delete_source_service(
    db: Session,
    source_id: int
):

    source = get_source_by_id(
        db,
        source_id
    )

    if not source:

        raise HTTPException(
            status_code=404,
            detail="Source not found"
        )

    delete_chunks_by_source_id(
        db,
        source_id
    )

    delete_vectors_by_source_id(
        source_id
    )

    delete_source_record(
        db,
        source
    )

    return {

        "message":
        "Source deleted successfully",

        "source_id":
        source_id
    }
