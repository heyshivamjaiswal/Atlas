from huggingface_hub import InferenceClient

from app.core.settings import (
    HUGGINGFACE_API_KEY,
    HF_EMBEDDING_MODEL
)

client = InferenceClient(
    api_key=HUGGINGFACE_API_KEY
)

vector = client.feature_extraction(
    "What is Docker?",
    model=HF_EMBEDDING_MODEL
)

print(type(vector))
print(len(vector))
