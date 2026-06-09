from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.services.source.pdf.processor import (
    process_pdf
)


async def process_pdf_source(
    file: UploadFile,
    db: Session
):

    return await process_pdf(
        file,
        db
    )


def process_website(
    url: str
):

    return {
        "message": "Website ingestion not implemented yet",
        "url": url
    }