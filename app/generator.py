def build_prompt(query, chunks):
    context_parts = []

    for index, chunk in enumerate(chunks, start=1):
        context_parts.append(
            f"[CHUNK {index}]: {chunk['text']}\n"
            f"Source: {chunk['metadata']['source']}, "
            f"Chunk {chunk['metadata']['chunk_index']}"
        )

    context = "\n\n".join(context_parts)

    prompt = (
        "You are a helpful assistant designed to answer questions accurately "
        "based only on the provided context.\n\n"
        "Do not use external knowledge.\n"
        "If the answer cannot be found in the context, respond with exactly: "
        "\"I don't know.\"\n\n"
        "Context:\n"
        "---\n"
        f"{context}\n"
        "---\n\n"
        f"Question: {query}\n\n"
        "Answer:"
    )

    return prompt


def generate_answer(query, chunks):
    if not chunks:
        return "I don't know."

    combined_text = " ".join(
        chunk["text"] for chunk in chunks
    )

    query_words = [
        word.lower()
        for word in query.split()
        if len(word) > 3
    ]

    matches = 0

    for word in query_words:
        if word in combined_text.lower():
            matches += 1

    if query_words and matches == 0:
        return "I don't know."

    return chunks[0]["text"]