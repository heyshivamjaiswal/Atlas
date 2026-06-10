from app.services.retrieval.retrieval_service import (
    retrieve_chunks
)

from app.services.llm.llm_service import (
    ask_llm
)


def answer_query(
    query: str,
    source_type: str | None = None
):

    retrieved = retrieve_chunks(
        query=query,
        source_type=source_type
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
You are a document QA assistant.

Rules:

- Use ONLY retrieved context
- Never invent facts
- If answer missing say:
  "Information not found in documents"
- Quote exact information when possible

Context:

{context}

Question:

{query}
"""
    print("\n===== PROMPT =====")
    print(prompt)

    answer = ask_llm(
        prompt
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