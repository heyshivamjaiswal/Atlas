from urllib.parse import urlparse

from fastapi import HTTPException


def validate_url(
    url: str
):
    parsed = urlparse(url)

    if not parsed.scheme or not parsed.netloc:

        raise HTTPException(
            status_code=400,
            detail="Invalid URL"
        )

    return url