from pathlib import Path

from config import KNOWLEDGE_BASE_PATH


def format_document_name(filename):
    stem = Path(filename).stem

    parts = stem.split("_", maxsplit=1)

    document_id = parts[0]

    if len(parts) == 1:
        return document_id

    title = parts[1].replace("_", " ")

    return {
        "id": document_id,
        "title": title,
    }


def get_knowledge_base():
    root = Path(KNOWLEDGE_BASE_PATH)

    base = {}

    for item in sorted(root.iterdir()):
        if item.is_dir():

            documents = []

            for file in sorted(item.iterdir()):
                if file.is_file():

                    documents.append(
                        format_document_name(file.name)
                    )

            base[item.name] = documents

    return base
