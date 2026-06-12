from sqlalchemy.orm import Session

from app.services.embedding.embedding_service import (
    embedding_model
)

from app.repositories.vector_repository import (
    search_vectors
)

from app.repositories.chunk_repository import (
    get_chunks_by_source_ids
)

from app.services.retrieval.bm25_service import (
    bm25_search
)


def retrieve_chunks(
    query: str,
    db: Session,
    user_id: int,
    top_k: int = 3,
    source_ids: list[int] | None = None
):

    seen = set()
    unique_results = []

    query_vector = embedding_model.embed_query(
        query
    )

    # VECTOR SEARCH
    print("\n===== RETRIEVAL FILTER =====")
    print("user_id =", user_id)
    print("source_ids =", source_ids)

    vector_results = search_vectors(
        query_vector=query_vector,
        limit=top_k,
        user_id=user_id,
        source_ids=source_ids
    )

    # BM25 SEARCH

    chunks = get_chunks_by_source_ids(
        db,
        source_ids or []
    )

    bm25_results = bm25_search(
        query=query,
        chunks=chunks,
        top_k=top_k
    )

    print("\n===== VECTOR RESULTS =====")

    for result in vector_results:

        print(
            result.payload.get(
                "content",
                ""
            )[:150]
        )

        print("----------------")

    print("\n===== BM25 RESULTS =====")

    for result in bm25_results:

        print(
            result["content"][:150]
        )

        print("----------------")

    print("\n===== RETRIEVED =====")

    for result in vector_results:

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
            result.payload.get(
                "content",
                ""
            )[:300]
        )

        print("----------------")

    return unique_results
