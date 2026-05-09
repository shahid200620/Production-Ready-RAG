from pathlib import Path
import re


def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def load_documents(data_dir="data"):
    documents = []

    for file_path in Path(data_dir).glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")
        text = clean_text(text)

        documents.append(
            {
                "text": text,
                "metadata": {
                    "source": file_path.name
                }
            }
        )

    return documents