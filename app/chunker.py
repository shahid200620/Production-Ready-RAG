def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])

        if end >= len(text):
            break

        start = end - overlap

    return chunks


def chunk_documents(documents, chunk_size=500, overlap=100):
    all_chunks = []

    for document in documents:
        text_chunks = chunk_text(
            document["text"],
            chunk_size=chunk_size,
            overlap=overlap
        )

        for index, chunk in enumerate(text_chunks):
            all_chunks.append(
                {
                    "text": chunk,
                    "metadata": {
                        "source": document["metadata"]["source"],
                        "chunk_index": index
                    }
                }
            )

    return all_chunks