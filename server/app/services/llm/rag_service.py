from app.services.retrieval.retrieval_service import (
    retrieve_chunks
)

from app.services.llm.llm_service import (
    ask_llm
)


def answer_query(
    query: str
):

    retrieved = retrieve_chunks(
        query
    )

    context = "\n\n".join(
        [
            item["chunk"]["content"]
            for item in retrieved
        ]
    )

    prompt = f"""
Context:

{context}

Question:

{query}

Answer using only provided context.
"""

    return ask_llm(
        prompt
    )