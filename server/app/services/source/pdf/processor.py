from fastapi import UploadFile

from app.services.source.pdf.chunk_mapper import (
    map_chunks
)

from app.services.embedding.embedding_service import (
    embed_chunks
)

from app.repositories.source_repository import (
    add_vectors,
    save_pdf_file,
    add_chunk,
)

from app.services.source.pdf.validator import (
    validator_pdf
)

from app.services.source.pdf.loader import (
    load_pdf_document
)

from app.services.source.pdf.splitter import (
    create_chunks
)


async def process_pdf(
    file: UploadFile
):

    # validation
    content = await validator_pdf(
        file
    )

    # save uploaded file
    file_path = save_pdf_file(
        file.filename,
        content
    )

    # load documents
    docs = load_pdf_document(
        file_path
    )

    # create chunks
    chunks = create_chunks(
        docs
    )

    # convert langchain chunks -> internal format
    mapped_chunks = map_chunks(
        chunks,
        file.filename
    )

    # store chunks
    add_chunk(
        mapped_chunks
    )

    # create embeddings
    vectors = embed_chunks(
        mapped_chunks
    )

    # combine chunk metadata + embeddings
    embedded_chunks = []

    for chunk, vector in zip(
        mapped_chunks,
        vectors
    ):

        embedded_chunks.append({

            **chunk,

            "embedding": vector
        })

    # store vectors with metadata
    add_vectors(
        embedded_chunks
    )

    return {

        "file_name": file.filename,

        "pages": len(docs),

        "chunks": len(mapped_chunks),

        "embeddings": len(vectors),

        "preview":
            chunks[0].page_content[:500]
            if chunks else ""
    }