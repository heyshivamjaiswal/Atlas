from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.source_repository import (
    get_sources,
    get_source_by_id_and_user,
    delete_source as delete_source_record,
    count_sources_by_type,
    get_sources_paginated
)

from app.repositories.chunk_repository import (
    count_chunks_by_source_id,
    delete_chunks_by_source_id,
    count_all_chunks_by_user,
    get_chunks_by_source_id
)

from app.repositories.vector_repository import (
    delete_vectors_by_source_id
)

from app.repositories.chat_session_source_repository import (
    delete_sessions_by_source
)

from app.services.storage.supabase_storage import (
    delete_pdf
)


def list_sources(
    db: Session,
    user_id: int
):

    sources = get_sources(
        db,
        user_id
    )

    result = []

    for source in sources:

        result.append({

            "id": source.id,

            "source_type": source.source_type,

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
    source_id: int,
    user_id: int
):

    source = get_source_by_id_and_user(
        db,
        source_id,
        user_id
    )

    if not source:

        raise HTTPException(
            status_code=404,
            detail="Source not found"
        )

    return {

        "id": source.id,

        "source_type": source.source_type,

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
    source_id: int,
    user_id: int
):

    source = get_source_by_id_and_user(
        db,
        source_id,
        user_id
    )

    if not source:

        raise HTTPException(
            status_code=404,
            detail="Source not found"
        )

    # 1. Delete vectors
    delete_vectors_by_source_id(
        source_id
    )

    # 2. Delete chunks
    delete_chunks_by_source_id(
        db,
        source_id
    )

    # 3. Delete chat ↔ source mappings
    delete_sessions_by_source(
        db,
        source_id
    )

    if source.storage_key:

        delete_pdf(
            source.storage_key
        )

    # 4. Delete source
    delete_source_record(
        db,
        source
    )

    return {
        "message": "Source deleted successfully",
        "source_id": source_id
    }


def get_source_stats(
    db: Session,
    user_id: int
):

    return {

        "total_sources":
        len(
            get_sources(
                db,
                user_id
            )
        ),

        "pdfs":
        count_sources_by_type(
            db,
            user_id,
            "pdf"
        ),

        "websites":
        count_sources_by_type(
            db,
            user_id,
            "website"
        ),

        "youtube":
        count_sources_by_type(
            db,
            user_id,
            "youtube"
        ),

        "total_chunks":
        count_all_chunks_by_user(
            db,
            user_id
        )
    }


def get_source_chunks(
    db: Session,
    source_id: int,
    user_id: int
):

    source = get_source_by_id_and_user(
        db,
        source_id,
        user_id
    )

    if not source:

        raise HTTPException(
            status_code=404,
            detail="Source not found"
        )

    chunks = get_chunks_by_source_id(
        db,
        source_id
    )

    return [
        {
            "chunk_index": chunk.chunk_index,
            "page": chunk.page,
            "content": chunk.content
        }

        for chunk in chunks
    ]


def list_sources_paginated(
    db: Session,
    user_id: int,
    search: str | None,
    skip: int,
    limit: int
):

    sources = get_sources_paginated(
        db,
        user_id,
        search,
        skip,
        limit
    )

    result = []

    for source in sources:

        result.append({

            "id": source.id,

            "source_type": source.source_type,

            "title": source.title,

            "chunk_count":
            count_chunks_by_source_id(
                db,
                source.id
            )
        })

    return result
