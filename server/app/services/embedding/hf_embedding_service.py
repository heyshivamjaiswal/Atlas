from huggingface_hub import InferenceClient

from app.core.settings import (
    HUGGINGFACE_API_KEY,
    HF_EMBEDDING_MODEL
)


class HFEmbeddingModel:

    def __init__(self):

        self.client = InferenceClient(
            api_key=HUGGINGFACE_API_KEY
        )

    def embed_query(
        self,
        text: str
    ):

        vector = self.client.feature_extraction(
            text,
            model=HF_EMBEDDING_MODEL
        )

        return vector.tolist()

    def embed_documents(
        self,
        texts: list[str]
    ):

        vectors = []

        for text in texts:

            vector = self.client.feature_extraction(
                text,
                model=HF_EMBEDDING_MODEL
            )

            vectors.append(
                vector.tolist()
            )

        return vectors


embedding_model = HFEmbeddingModel()
