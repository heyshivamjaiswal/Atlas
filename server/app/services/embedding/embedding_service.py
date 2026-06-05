from langchain_ollama import OllamaEmbeddings

embedding_model = OllamaEmbeddings(
    model="nomic-embedd-text"
)

def embed_chunks(chunks):
    
    text = [
        chunk["content"]
        for chunk in chunks
    ]

    vectors = embedding_model.embed_documents(text)

    return vectors