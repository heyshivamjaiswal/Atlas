from fastapi import UploadFile

from app.services.source.pdf.chunk_mapper import map_chunks

from app.repositories.source_repository import save_pdf_file, add_chunk

from app.services.source.pdf.validator import  validator_pdf

from app.services.source.pdf.loader import  load_pdf_document

from app.services.source.pdf.splitter import create_chunks

async def process_pdf(file: UploadFile):

    content = await validator_pdf(file)

    file_path = save_pdf_file(
        file.filename,
        content
    )

    docs = load_pdf_document(file_path)

    chunks = create_chunks(docs)

    mapped_chunks = map_chunks(chunks, file.filename)

    add_chunk(mapped_chunks)

    return {
        "file_name": file.filename,
        "pages": len(docs),
        "chunks": len(mapped_chunks),
        "preview": chunks[0].page_content[:500]
        if chunks else ""
    }