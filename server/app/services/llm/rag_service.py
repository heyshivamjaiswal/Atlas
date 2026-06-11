from sqlalchemy.orm import Session

from app.services.retrieval.retrieval_service import (
    retrieve_chunks
)

from app.services.llm.llm_service import (
    ask_llm
)


def answer_query(
    query: str,
    db: Session,
    user_id: int,
    source_type: str | None = None,
    source_id: int | None = None
):

    retrieved = retrieve_chunks(
        query=query,
        db=db,
        user_id=user_id,
        source_type=source_type,
        source_id=source_id
    )

    if not retrieved:

        return {
            "answer":
            "Information not found in documents.",
            "sources": []
        }

    context = "\n\n".join(
        [
            item.payload["content"]
            for item in retrieved
        ]
    )

    print(
        "\n===== CONTEXT ====="
    )

    print(
        context[:1000]
    )

    prompt = f"""
Answer the question using ONLY the provided context.

If the answer exists in the context, answer directly.

If the answer does not exist in the context, reply exactly:

Information not found in documents.

Context:

{context}

Question:

{query}

Answer:
"""

    print(
        "\n===== PROMPT ====="
    )

    print(
        prompt
    )

    answer = ask_llm(
        prompt
    )

    print(
        "\n===== ANSWER ====="
    )

    print(
        answer
    )

    sources = []

    for item in retrieved:

        sources.append({

            "source": item.payload["source"],

            "page": item.payload["page"],

            "score": round(
                item.score,
                3
            )
        })

    return {

        "answer": answer,

        "sources": sources
    }
