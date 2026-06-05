from fastapi import UploadFile

from app.repositories.source_repository import save_pdf_file

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

    return {
        "file_name": file.filename,
        "pages": len(docs),
        "chunks": len(chunks),
        "preview": chunks[0].page_content[:500]
        if chunks else ""
    }