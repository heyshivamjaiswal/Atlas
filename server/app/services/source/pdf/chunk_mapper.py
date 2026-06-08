def map_chunks(
    chunks,
    file_name: str,
    source_id: int
):

    mapped = []

    for index, chunk in enumerate(chunks):

        mapped.append({

            "source_id": source_id,

            "chunk_index": index,

            "content": chunk.page_content,

            "page": chunk.metadata.get(
                "page",
                0
            ),

            "source": file_name
        })

    return mapped