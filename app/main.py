import argparse

from app.retriever import retrieve
from app.generator import generate_answer


def main():
    parser = argparse.ArgumentParser(
        description="Production-Ready RAG Pipeline"
    )

    parser.add_argument(
        "question",
        nargs="+",
        help="Question to ask the RAG system"
    )

    parser.add_argument(
        "--top-k",
        type=int,
        default=3,
        help="Number of chunks to retrieve"
    )

    args = parser.parse_args()

    query = " ".join(args.question)

    print()
    print("Searching knowledge base...")
    print()

    chunks = retrieve(query, top_k=args.top_k)
    answer = generate_answer(query, chunks)

    print("Answer:")
    print(answer)
    print()

    print("Sources:")
    print()

    for chunk in chunks:
        metadata = chunk["metadata"]

        print(
            f"- {metadata['source']} "
            f"(chunk {metadata['chunk_index']})"
        )
        print(chunk["text"])
        print()


if __name__ == "__main__":
    main()