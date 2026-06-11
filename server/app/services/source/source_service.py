from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.services.source.pdf.processor import (
    process_pdf
)

from app.services.source.web.processor import (
    process_website as process_website_source
)

from app.services.source.youtube.processor import (
    process_youtube as youtube_processor
)


async def process_pdf_source(
    file: UploadFile,
    db: Session,
    user_id: int
):

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
