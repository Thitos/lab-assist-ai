import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

EMBEDDING_MODEL = "gemini-embedding-001"
LLM_MODEL = "gemini-3.5-flash"

KNOWLEDGE_BASE_PATH = "knowledge_base"
VECTOR_STORE_PATH = "vector_store"

CATEGORY_LABELS = {
    "01_onboarding": "Onboarding",
    "02_biosafety": "Biossegurança",
    "03_protocols": "Protocolos",
    "04_equipment": "Equipamentos",
    "05_administrative": "Administrativo",
}

CHUNK_SIZE = 2000
CHUNK_OVERLAP = 300

BATCH_SIZE = 25
DELAY_SECONDS = 35
EVALUATION_DELAY_SECONDS = 20

RETRIEVAL_K = 4
SIMILARITY_THRESHOLD = 0.65
TEMPERATURE = 0.2