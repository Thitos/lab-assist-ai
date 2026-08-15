import time

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import (
    DirectoryLoader,
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
)

from config import (
    GEMINI_API_KEY,
    EMBEDDING_MODEL,
    KNOWLEDGE_BASE_PATH,
    VECTOR_STORE_PATH,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    BATCH_SIZE,
    DELAY_SECONDS,
)

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY has not been configured.")

def load_documents():
    """Loads PDF, DOCX, and Markdown documents from the knowledge base."""
    documents = []

    loaders = [
        ("**/*.pdf", PyPDFLoader),
        ("**/*.docx", Docx2txtLoader),
        ("**/*.md", TextLoader),
    ]

    for file_pattern, loader_class in loaders:
        try:
            loader = DirectoryLoader(
                path=KNOWLEDGE_BASE_PATH,
                glob=file_pattern,
                loader_cls=loader_class,
                recursive=True,
                use_multithreading=True,
            )

            docs = loader.load()
            documents.extend(docs)

            print(f"{file_pattern}: {len(docs)} documents")

        except Exception as error:
            print(f"Error loading {file_pattern}: {error}")

    return documents

# Uploads the documents
documents = load_documents()

if not documents:
    raise ValueError(
        "No documents were found in the knowledge base."
    )

print(f"Total documents loaded: {len(documents)}")

# Creating embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model=EMBEDDING_MODEL,
    google_api_key=GEMINI_API_KEY,
)

# Splitting documents into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    separators=["\n\n", "\n", ". ", " ", ""],
)

chunks = text_splitter.split_documents(documents)

if not chunks:
    raise ValueError("No chunks were created from the documents.")

print(f"Chunks generated: {len(chunks)}")

# Creating the vector database
print("Creating vector database...")

vector_store = None

for i in range(0, len(chunks), BATCH_SIZE):
    batch = chunks[i:i + BATCH_SIZE]
    batch_number = i // BATCH_SIZE + 1

    print(f"Processing batch {batch_number}...")

    try:
        if vector_store is None:
            vector_store = FAISS.from_documents(batch, embeddings)
        else:
            vector_store.add_documents(batch)

    except Exception as error:
        raise RuntimeError(
            f"Error processing batch {batch_number}: {error}"
        )

    if i + BATCH_SIZE < len(chunks):
        time.sleep(DELAY_SECONDS)

if vector_store is None:
    raise RuntimeError("Could not create vector database.")

vector_store.save_local(VECTOR_STORE_PATH)

print("Vector database created successfully!")