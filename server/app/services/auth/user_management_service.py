from app.repositories.source_repository import (
    get_source_ids_by_user,
    delete_sources_by_user_id
)

from app.repositories.chunk_repository import (
    delete_chunks_by_source_id
)

from app.repositories.vector_repository import (
    delete_vectors_by_source_id
)

from app.repositories.user_repository import (
    delete_user
)


def delete_current_user(
    db,
    current_user
):

    source_ids = get_source_ids_by_user(
        db,
        current_user.id
    )

    for source_id in source_ids:

        delete_vectors_by_source_id(
            source_id
        )

        delete_chunks_by_source_id(
            db,
            source_id
        )

    delete_sources_by_user_id(
        db,
        current_user.id
    )

    delete_user(
        db,
        current_user
    )

    return {
        "message": "User deleted successfully"
    }
