FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p vector_store

CMD ["python", "-m", "app.main", "What are the two phases of a RAG pipeline?"]