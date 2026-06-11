from app.services.embedding.embedding_service import (
    embedding_model
)

from app.repositories.vector_repository import (
    search_vectors
)


def retrieve_chunks(
    query: str,
    top_k: int = 5,
    source_type: str | None = None,
    source_id: int | None = None
):

    query_vector = embedding_model.embed_query(
        query
    )

    results = search_vectors(
        query_vector=query_vector,
        limit=top_k,
        source_type=source_type,
        source_id=source_id

    )

    print(
        f"\nFiltering by source_type: {source_type}"
    )

    print("\n===== RETRIEVED =====")

    for result in results:

        print(
            f"Score: {round(result.score, 3)}"
        )

        print(
            result.payload.get(
                "content",
                ""
            )[:300]
        )

        print("----------------")

    return results
