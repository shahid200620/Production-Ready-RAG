import os

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import chromadb


def retrieve(query, top_k=3):
    load_dotenv()

    embedding_model_name = os.getenv(
        "EMBEDDING_MODEL",
        "all-MiniLM-L6-v2"
    )

    model = SentenceTransformer(embedding_model_name)

    chroma_client = chromadb.PersistentClient(path="vector_store")
    collection = chroma_client.get_collection(
        name="rag_documents"
    )

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    chunks = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    for document, metadata in zip(documents, metadatas):
        chunks.append(
            {
                "text": document,
                "metadata": metadata
            }
        )

    return chunks