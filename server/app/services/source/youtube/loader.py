from langchain_community.document_loaders import (
    YoutubeLoader
)


def load_youtube_document(
    url: str
):
    loader = YoutubeLoader.from_youtube_url(
        url
    )

    return loader.load()