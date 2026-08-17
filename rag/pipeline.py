from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)

from config import (
    GEMINI_API_KEY,
    EMBEDDING_MODEL,
    LLM_MODEL,
    VECTOR_STORE_PATH,
    RETRIEVAL_K,
    SIMILARITY_THRESHOLD,
    TEMPERATURE,
)

from prompts import RAG_PROMPT

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY has not been configured.")

# Load embedding model
embeddings = GoogleGenerativeAIEmbeddings(
    model=EMBEDDING_MODEL,
    google_api_key=GEMINI_API_KEY,
)

# Load vector database
vector_store = None

try:
    vector_store = FAISS.load_local(
        VECTOR_STORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True,
    )
except Exception as error:
    print(f"ERROR: Could not load vector database: {error}")

# Initialize language model
llm = ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    google_api_key=GEMINI_API_KEY,
    temperature=TEMPERATURE,
)

def ask_question(query):
    """
    Search the knowledge base and generate an answer.
    """

    if not query or not query.strip():
        return {
            "answer": "Digite uma pergunta para consultar a documentação do laboratório.",
            "sources": [],
        }

    if vector_store is None:
        return {
            "answer": (
                "Não foi possível acessar a base de documentos do laboratório "
                "neste momento. Verifique a configuração da aplicação."
            ),
            "sources": [],
        }

    # Retrieve documents with similarity scores
    try:
        docs_with_scores = (
            vector_store.similarity_search_with_score(
                query,
                k=RETRIEVAL_K,
            )
        )
        print("\n=== RETRIEVED DOCUMENTS ===")
        
        for i, (doc, score) in enumerate(docs_with_scores, start=1):
            print(f"\nDocument {i}")
            print(f"Score: {score:.4f}")
            print(
                "Source:",
                doc.metadata.get("source", "unknown source")
            )

    except Exception as error:
        raise RuntimeError(
            f"Error retrieving documents: {error}"
        )

    # No documents found
    if not docs_with_scores:
        return {
            "answer": (
                 "Não encontrei essa informação na documentação disponível "
                 "do laboratório.\n\n"
                 "Se quiser, tente reformular a pergunta ou consulte o "
                 "responsável pelo procedimento."
            ),
            "sources": [],
        }

    # Get the best similarity score
    best_score = docs_with_scores[0][1]

    # Check similarity threshold
    if best_score > SIMILARITY_THRESHOLD:
        return {
            "answer": (
                "Não encontrei essa informação na documentação disponível "
                "do laboratório.\n\n"
                "Se quiser, tente reformular a pergunta ou consulte o "
                "responsável pelo procedimento."
            ),
            "sources": [],
        }

    # Get retrieved documents
    docs = [
        doc
        for doc, score in docs_with_scores
    ]

    # Build context
    context_parts = []

    for i, doc in enumerate(docs, start=1):

        source = doc.metadata.get(
            "source",
            "fonte desconhecida"
        )

        context_parts.append(
            f"""
[CONTEXTO {i}]
Fonte: {source}

{doc.page_content}
"""
        )

    context = "\n\n--------------------\n\n".join(
        context_parts
    )

    # Create prompt
    prompt = PromptTemplate.from_template(
        RAG_PROMPT
    )

    # Generate answer
    rag_chain = prompt | llm

    try:
        answer = rag_chain.invoke({
            "context": context,
            "query": query,
        })
    except Exception as error:
        raise RuntimeError(
            f"Error generating the answer: {error}"
        )

    # Extract answer text
    answer_text = answer.content

    if isinstance(answer_text, list):
        answer_text = answer_text[0]["text"]
    
    answer_text = answer_text.strip()

    # Get source names
    sources = []

    for doc in docs:

        source = doc.metadata.get("source")

        if source:

            source_name = source.split("/")[-1]

            if source_name not in sources:
                sources.append(source_name)

    return {
        "answer": answer_text,
        "sources": sources,
    }