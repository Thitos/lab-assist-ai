import json
import time

from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)

from prompts import RAG_PROMPT
from config import (
    GEMINI_API_KEY,
    EMBEDDING_MODEL,
    LLM_MODEL,
    VECTOR_STORE_PATH,
    RETRIEVAL_K,
    SIMILARITY_THRESHOLD,
    TEMPERATURE,
    EVALUATION_DELAY_SECONDS,
)

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY has not been configured.")

# Questions to test
# Select the question IDs manually to limit API usage.
# The free-tier API has daily request limits.
TEST_QUESTIONS = [
    1,
    4,
    9,
    11,
    21,
    28,
]

# Loading embedding model
embeddings = GoogleGenerativeAIEmbeddings(
    model=EMBEDDING_MODEL,
    google_api_key=GEMINI_API_KEY,
)

# Loading vector database
print("Loading vector database...")

try:
    vector_store = FAISS.load_local(
        VECTOR_STORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True,
    )
except Exception as error:
    raise RuntimeError(
        f"Could not load vector database: {error}"
    )

# Initializing language model
llm = ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    google_api_key=GEMINI_API_KEY,
    temperature=TEMPERATURE,
)

# Loading evaluation questions
with open(
    "evaluation/questions.json",
    "r",
    encoding="utf-8"
) as file:
    data = json.load(file)

results = []

# Evaluate each question
for question in data["questions"]:

    question_id = question["id"]

    # Skip questions that are not in the test list
    if question_id not in TEST_QUESTIONS:
        continue

    area = question["area"]
    query = question["question"]

    print(f"\nQuestion {question_id}: {query}")

    # Retrieve documents and similarity scores
    try:
        docs_with_scores = (
            vector_store.similarity_search_with_score(
                query,
                k=RETRIEVAL_K,
            )
        )
    except Exception as error:
        print(f"Error retrieving documents: {error}")
        continue

    if not docs_with_scores:
        print("No relevant documents were found.")
        continue

    # Get the score of the best document
    best_score = docs_with_scores[0][1]

    print(f"Best score: {best_score:.4f}")
    print(f"Threshold: {SIMILARITY_THRESHOLD}")

    # Check similarity threshold
    if best_score > SIMILARITY_THRESHOLD:

        answer_text = (
            "Não encontrei essa informação "
            "na documentação disponível."
        )

        print("\n=== LabAssistAI ===")
        print(answer_text)

        results.append({
            "id": question_id,
            "area": area,
            "question": query,
            "best_score": float(best_score),
            "threshold": SIMILARITY_THRESHOLD,
            "retrieval_accepted": False,
            "retrieved_sources": [],
            "answer": answer_text,
        })

        continue

    # Create the context using the retrieved documents
    docs = [
        doc
        for doc, score in docs_with_scores
    ]

    context_parts = []
    
    for i, doc in enumerate(docs, start=1):
        source = doc.metadata.get("source", "fonte desconhecida")
    
        context_parts.append(
            f"""
    [CONTEXTO {i}]
    Fonte: {source}
    
    {doc.page_content}
    """
        )
    
    context = "\n\n--------------------\n\n".join(context_parts)
  
    # Prompt
    prompt = PromptTemplate.from_template(RAG_PROMPT)
        
        # Generate the answer
    rag_chain = prompt | llm
    try:
        answer = rag_chain.invoke({
            "context": context,
            "query": query
        })
    except Exception as error:
        print(f"Error generating the answer: {error}")
        continue

    answer_text = answer.content[0]["text"].strip()

    print("\n=== LabAssistAI ===")
    print(answer_text)

    # Get retrieved source names
    retrieved_sources = []

    for doc in docs:

        source = doc.metadata.get("source")

        if source:

            source_name = source.split("/")[-1]

            if source_name not in retrieved_sources:
                retrieved_sources.append(source_name)

    # Save result
    results.append({
        "id": question_id,
        "area": area,
        "question": query,
        "best_score": float(best_score),
        "threshold": SIMILARITY_THRESHOLD,
        "retrieval_accepted": True,
        "retrieved_sources": retrieved_sources,
        "answer": answer_text,
    })

    # Wait before the next API request
    time.sleep(EVALUATION_DELAY_SECONDS)

# Save all results
with open(
    "evaluation/gemini_results.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        results,
        file,
        ensure_ascii=False,
        indent=2,
    )

print("\nEvaluation completed.")
print(
    "Results saved to "
    "evaluation/gemini_results.json"
)