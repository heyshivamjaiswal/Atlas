def map_chunks(
    chunks,
    source: str,
    source_id: int,
    source_type: str,
    user_id: int
):

    mapped = []

    for index, chunk in enumerate(chunks):

        mapped.append({

            "source_id": source_id,

            "source_type": source_type,

            "user_id": user_id,

            "chunk_index": index,

            "content": chunk.page_content,

            "page": chunk.metadata.get(
                "page",
                0
            ),

            "source": source
        })

    return mapped
