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
    You are a retrieval assistant.

Rules:

- ONLY answer using context
- If answer is missing say:
  "Information not found in documents"
- Do not invent information

Context:

{context}

Question:

{query}
"""

    return ask_llm(
        prompt
    )