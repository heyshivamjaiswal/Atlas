from app.services.embedding.embedding_service import (
    embedding_model
)

from app.repositories.vector_repository import (
    search_vectors
)


def debug_retrieval(
    query: str,
    user_id: int
):

    query_vector = embedding_model.embed_query(
        query
    )

    results = search_vectors(
        query_vector,
        limit=5,
        user_id=user_id
    )

    return [

        {
            "score": result.score,

            "source":
            result.payload.get(
                "source"
            ),

            "page":
            result.payload.get(
                "page"
            ),

            "content":
            result.payload.get(
                "content"
            )
        }

        for result in results
    ]
