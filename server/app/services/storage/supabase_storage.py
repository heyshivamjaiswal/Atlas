from supabase import create_client

from app.core.settings import (
    SUPABASE_URL,
    SUPABASE_KEY,
    SUPABASE_BUCKET
)

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


def upload_pdf(
    file_name: str,
    content: bytes
):

    response = supabase.storage.from_(
        SUPABASE_BUCKET
    ).upload(
        path=file_name,
        file=content
    )

    return response
