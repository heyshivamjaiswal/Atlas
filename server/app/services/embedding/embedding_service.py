from langchain_ollama import OllamaEmbeddings

embedding_model = OllamaEmbeddings(
    model="nomic-embed-text"
)

def embed_chunks(chunks):
    
    text = [
        chunk["content"]
        for chunk in chunks
    ]

    vectors = embedding_model.embed_documents(text)

    return vectors