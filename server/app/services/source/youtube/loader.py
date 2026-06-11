from fastapi import HTTPException
from langchain_community.document_loaders import YoutubeLoader


def load_youtube_document(
    url: str
):

    try:

        loader = YoutubeLoader.from_youtube_url(
            url,
            language=["hi", "en"]
        )

        return loader.load()

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=f"Unable to fetch transcript: {str(e)}"
        )
