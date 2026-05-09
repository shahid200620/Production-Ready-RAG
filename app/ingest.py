import os

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import chromadb

from app.loader import load_documents
from app.chunker import chunk_documents


def ingest():
    load_dotenv()

    embedding_model_name = os.getenv(
        "EMBEDDING_MODEL",
        "all-MiniLM-L6-v2"
    )

    print("Loading embedding model...")
    model = SentenceTransformer(embedding_model_name)

    chroma_client = chromadb.PersistentClient(path="vector_store")
    collection = chroma_client.get_or_create_collection(
        name="rag_documents"
    )

    documents = load_documents()
    chunks = chunk_documents(documents)

    if collection.count() > 0:
        existing = collection.get()
        if existing["ids"]:
            collection.delete(ids=existing["ids"])

    for index, chunk in enumerate(chunks):
        embedding = model.encode(
            chunk["text"]
        ).tolist()

        chunk_id = f"chunk_{index}"

        collection.add(
            ids=[chunk_id],
            documents=[chunk["text"]],
            embeddings=[embedding],
            metadatas=[chunk["metadata"]]
        )

        print(f"Stored {chunk_id}")

    print()
    print(f"Ingestion complete. Stored {len(chunks)} chunks.")


if __name__ == "__main__":
    ingest()