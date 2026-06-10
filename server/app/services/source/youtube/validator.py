from urllib.parse import urlparse

from fastapi import HTTPException


def validator_youtube(
    url: str
):
    parsed = urlparse(url)

    if not parsed.scheme or not parsed.netloc:

        raise HTTPException(
            status_code=400,
            detail="Invalid URL"
        )

    allowed_domains = [

        "youtube.com",

        "www.youtube.com",

        "youtu.be"
    ]

    if parsed.netloc not in allowed_domains:

        raise HTTPException(
            status_code=400,
            detail="URL must be a YouTube link"
        )

    return url