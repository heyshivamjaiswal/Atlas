from app.services.embedding.embedding_service import (
    embedding_model
)

from app.repositories.vector_repository import (
    search_vectors
)


def retrieve_chunks(
    query: str,
    top_k: int = 3,
    source_type: str | None = None,
    source_id: int | None = None
):

    seen = set()
    unique_results = []

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

        content = result.payload["content"]

        if content in seen:
            continue

        seen.add(content)
        unique_results.append(result)

        print(
            f"""
            Source ID: {result.payload.get("source_id")}
            Source Type: {result.payload.get("source_type")}
            Score: {round(result.score, 3)}
            """
        )
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

    return unique_results
