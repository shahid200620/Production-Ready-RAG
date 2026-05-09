\# Production-Ready RAG Pipeline



A Retrieval-Augmented Generation (RAG) pipeline built from scratch using Python, Sentence Transformers, Chroma, and Docker.



\## Features



\- Document ingestion from `.txt` files

\- Text chunking with overlap

\- Local embeddings using Sentence Transformers

\- Persistent vector storage with Chroma

\- Semantic similarity search

\- Context-grounded answer generation

\- Source citations with metadata

\- Docker and Docker Compose support



\---



\## Tech Stack



\- Python 3.11

\- Sentence Transformers

\- ChromaDB

\- Docker

\- Docker Compose

\- python-dotenv



\---



\## Project Structure



```text

Production-Ready-RAG/

├── app/

│   ├── loader.py

│   ├── chunker.py

│   ├── ingest.py

│   ├── retriever.py

│   ├── generator.py

│   └── main.py

├── data/

├── vector\_store/

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

├── .env.example

└── README.md

```



\---



\## Setup



\### Clone Repository



```bash

git clone https://github.com/shahid200620/Production-Ready-RAG.git

cd Production-Ready-RAG

```



\### Create Virtual Environment



```bash

python -m venv venv

venv\\Scripts\\activate

```



\### Install Dependencies



```bash

pip install -r requirements.txt

```



\### Create Environment File



```bash

copy .env.example .env

```



\---



\## Build Vector Store



```bash

python -m app.ingest

```



\---



\## Run Application



```bash

python -m app.main "What are the two phases of a RAG pipeline?"

```



\---



\## Example Questions



\- What are the two phases of a RAG pipeline?

\- How does RAG reduce hallucinations?

\- What is cosine similarity?

\- What is Chroma?

\- What are embeddings?



\---



\## Docker



\### Build Image



```bash

docker build -t production-ready-rag .

```



\### Run Container



```bash

docker run --rm production-ready-rag

```



\---



\## Docker Compose



```bash

docker compose up --build

```



\---



\## Environment Variables



| Variable | Description |

|----------|-------------|

| EMBEDDING\_MODEL | Sentence Transformer model |

| CHAT\_MODEL | Generation strategy |



\---



\## Design Choices



\- Sentence Transformers are used for free local embeddings.

\- Chroma is used as a persistent vector database.

\- Chunk overlap helps preserve context during retrieval.

\- Answers are generated strictly from retrieved context.

\- The system returns `"I don't know."` when relevant information is unavailable.



\---



\## Future Improvements



\- PDF support

\- Hybrid search

\- Re-ranking

\- Web interface

\- Hosted LLM integration



\---



\## License



Educational and portfolio use.

