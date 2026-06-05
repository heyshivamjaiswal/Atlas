def map_chunks(
        chunks,
        file_name: str
):
    mapped_chunks = []

    for index , chunk in enumerate(chunks):

        mapped_chunks.append({
            "chunk_id": index +1,

            "source": file_name,

            "page": chunk.metadata.get('page', None),

           "content": chunk.page_content
        })

    return mapped_chunks    