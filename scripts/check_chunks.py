from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader

from config import (
    KNOWLEDGE_BASE_PATH,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)

# Document to inspect
# Update this path manually before running the script.
DOCUMENT_PATH = (
    Path(KNOWLEDGE_BASE_PATH)
    / "03_protocols"
    / "POP-RNA-001_Protocolo_Extracao_RNA_Total_TRIzol.md"
)

# Select loader based on file extension
suffix = DOCUMENT_PATH.suffix.lower()

if suffix == ".pdf":
    loader = PyPDFLoader(str(DOCUMENT_PATH))

elif suffix == ".md":
    loader = TextLoader(
        str(DOCUMENT_PATH),
        encoding="utf-8",
    )

else:
    raise ValueError(
        f"Unsupported file type: {suffix}"
    )

# Load document
documents = loader.load()

print(f"Pages loaded: {len(documents)}")

# Create chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    separators=["\n\n", "\n", ". ", " ", ""],
)

chunks = text_splitter.split_documents(documents)

print(f"Chunks generated: {len(chunks)}")

# Show chunks
for number, chunk in enumerate(chunks, start=1):

    #text = chunk.page_content.lower()

    print("\n" + "=" * 60)
    print(f"CHUNK {number}")
    print("=" * 60)

    print(chunk.page_content)
