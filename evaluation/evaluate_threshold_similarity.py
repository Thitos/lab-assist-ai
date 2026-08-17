import json

from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config import (
    GEMINI_API_KEY,
    EMBEDDING_MODEL,
    VECTOR_STORE_PATH,
    SIMILARITY_THRESHOLD,
)

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY has not been configured.")

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

# Loading evaluation questions
with open(
    "evaluation/questions.json",
    "r",
    encoding="utf-8"
) as file:
    data = json.load(file)

results = []

# Evaluate similarity scores
for question in data["questions"]:

    question_id = question["id"]
    area = question["area"]
    query = question["question"]
    answerable = question["answerable"]

    print(f"\nQuestion {question_id}: {query}")

    try:
        docs_with_scores = (
            vector_store.similarity_search_with_score(
                query,
                k=1,
            )
        )
    except Exception as error:
        print(f"Error during search: {error}")
        continue

    if not docs_with_scores:
        print("No documents found.")
        continue

    doc, score = docs_with_scores[0]

    source = doc.metadata.get("source")

    if source:
        source_name = source.split("/")[-1]
    else:
        source_name = None

    # Apply threshold
    if score <= SIMILARITY_THRESHOLD:
        decision = "accept"
    else:
        decision = "reject"

    result = {
        "id": question_id,
        "area": area,
        "question": query,
        "answerable": answerable,
        "top_source": source_name,
        "top_score": float(score),
        "threshold": SIMILARITY_THRESHOLD,
        "decision": decision,
    }

    results.append(result)

    print(f"Answerable: {answerable}")
    print(f"Top source: {source_name}")
    print(f"Top score: {score:.4f}")
    print(f"Decision: {decision}")

# Print summary

print("\n" + "=" * 40)
print("=== THRESHOLD EVALUATION ===")
print("=" * 40)

answerable_accepted = 0
answerable_rejected = 0
not_answerable_accepted = 0
not_answerable_rejected = 0

for result in results:

    if result["answerable"]:

        if result["decision"] == "accept":
            answerable_accepted += 1
        else:
            answerable_rejected += 1

    else:

        if result["decision"] == "accept":
            not_answerable_accepted += 1
        else:
            not_answerable_rejected += 1

print(f"\nThreshold: {SIMILARITY_THRESHOLD}")

print("\nAnswerable questions:")
print(f"Accepted: {answerable_accepted}")
print(f"Rejected: {answerable_rejected}")

print("\nNot answerable questions:")
print(f"Accepted: {not_answerable_accepted}")
print(f"Rejected: {not_answerable_rejected}")

# Save results

with open(
    "evaluation/threshold_results.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        results,
        file,
        ensure_ascii=False,
        indent=2,
    )

print("\nThreshold evaluation completed.")
print(
    "Results saved to "
    "evaluation/threshold_results.json"
)