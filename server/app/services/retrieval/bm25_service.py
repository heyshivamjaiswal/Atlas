from rank_bm25 import BM25Okapi


def bm25_search(
    query: str,
    chunks: list,
    top_k: int = 5
):

    corpus = [
        chunk.content
        for chunk in chunks
    ]

    tokenized_corpus = [
        doc.split()
        for doc in corpus
    ]

    bm25 = BM25Okapi(
        tokenized_corpus
    )

    tokenized_query = query.split()

    scores = bm25.get_scores(
        tokenized_query
    )

    ranked = sorted(
        zip(chunks, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        {
            "content": chunk.content,
            "page": chunk.page,
            "source_id": chunk.source_id,
            "score": float(score),
            "type": "bm25"
        }
        for chunk, score in ranked[:top_k]
    ]
