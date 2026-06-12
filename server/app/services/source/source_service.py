from app.services.source.youtube.processor import (
    process_youtube as youtube_processor
)
from app.services.source.web.processor import (
    process_website as process_website_source
)
from app.services.source.pdf.processor import (
    process_pdf
)
from sqlalchemy.orm import Session
from fastapi import UploadFile
print("SOURCE_SERVICE_LOADED")


async def process_pdf_source(
    file: UploadFile,
    db: Session,
    user_id: int
):
    print("PROCESS_PDF_SOURCE_NEW_VERSION")

    return await process_pdf(
        file,
        db,
        user_id
    )


def process_website(
    url: str,
    db: Session,
    user_id: int
):

    return process_website_source(
        url,
        db,
        user_id
    )


def process_youtube_source(
    url: str,
    db: Session,
    user_id: int
):

    return youtube_processor(
        url,
        db,
        user_id
    )
