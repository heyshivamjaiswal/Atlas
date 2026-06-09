from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.repositories.source_repository import (
    create_source
)

from app.services.source.pdf.storage import (
    save_pdf_file
)

from app.repositories.chunk_repository import (
    create_chunks as create_chunk_records
)

from app.services.source.pdf.chunk_mapper import (
    map_chunks
)

from app.services.embedding.embedding_service import (
    embed_chunks
)

from app.services.source.pdf.validator import (
    validator_pdf
)

from app.services.source.pdf.loader import (
    load_pdf_document
)

from app.services.source.pdf.splitter import (
    create_chunks as split_chunks
)


async def process_pdf(
    file: UploadFile,
    db: Session
):

    # validate file
    content = await validator_pdf(
        file
    )

    # save pdf locally
    file_path = save_pdf_file(

        file.filename,

        content
    )

    # load document
    docs = load_pdf_document(
        file_path
    )

    # split document
    chunks = split_chunks(
        docs
    )

    # create source row
    source = create_source(

        db=db,

        user_id=1,  # temp until auth

        source_type="pdf",

        title=file.filename,

        file_name=file.filename
    )

    # map chunks
    mapped_chunks = map_chunks(

        chunks,

        file.filename,

        source.id
    )

    # persist chunks
    create_chunk_records(

        db=db,

        chunks=mapped_chunks
    )

    # embeddings (temporary still in memory)
    vectors = embed_chunks(
        mapped_chunks
    )

    return {

        "file_name": file.filename,

        "source_id": source.id,

        "pages": len(docs),

        "chunks": len(mapped_chunks),

        "embeddings": len(vectors),

        "preview":

            chunks[0].page_content[:500]

            if chunks else ""
    }