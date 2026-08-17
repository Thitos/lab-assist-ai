import json

from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config import (
    GEMINI_API_KEY,
    EMBEDDING_MODEL,
    VECTOR_STORE_PATH,
    RETRIEVAL_K,
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

# Evaluating retriever
results = []

rank_1_count = 0
top_k_count = 0
miss_count = 0

answerable_count = 0
not_answerable_count = 0

for question in data["questions"]:

    question_id = question["id"]
    area = question["area"]
    query = question["question"]
    answerable = question["answerable"]
    expected_sources = question["expected_sources"]

    print(f"\nQuestion {question_id}: {query}")

    # Search documents and get their scores
    try:
        docs_with_scores = vector_store.similarity_search_with_score(
            query,
            k=RETRIEVAL_K,
        )
    except Exception as error:
        print(f"Error during search: {error}")
        continue

    # Get source names and scores from retrieved documents
    retrieved_sources = []
    retrieved_scores = []

    for doc, score in docs_with_scores:

        source = doc.metadata.get("source")

        if source:
            source_name = source.split("/")[-1]

            retrieved_sources.append(source_name)
            retrieved_scores.append(score)

    # Find the expected document
    rank = None
    matched_source = None
    matched_score = None

    for position, source in enumerate(
        retrieved_sources,
        start=1
    ):

        if source in expected_sources:

            rank = position
            matched_source = source
            matched_score = retrieved_scores[position - 1]

            break

    # Evaluate answerable questions
    if answerable:

        answerable_count += 1

        if rank == 1:

            rank_1_count += 1
            top_k_count += 1
            result_status = "rank_1"

        elif rank is not None:

            top_k_count += 1
            result_status = "top_k"

        else:

            miss_count += 1
            result_status = "miss"

    # Evaluate questions without an expected answer
    else:

        not_answerable_count += 1
        result_status = "not_answerable"

    # Create result
    result = {
        "id": question_id,
        "area": area,
        "question": query,
        "answerable": answerable,
        "expected_sources": expected_sources,
        "matched_source": matched_source,
        "rank": rank,
        "found_in_top_k": rank is not None,
        "score": (float(matched_score) if matched_score is not None else None),
        "status": result_status,
        "retrieved_sources": retrieved_sources,
    }

    results.append(result)

    # Print result
    print(f"Expected: {expected_sources}")
    print(f"Retrieved: {retrieved_sources}")
    print(f"Rank: {rank}")
    print(f"Score: {matched_score}")
    print(f"Status: {result_status}")

# Calculate percentages
if answerable_count > 0:

    rank_1_percentage = (
        rank_1_count / answerable_count
    ) * 100

    top_k_percentage = (
        top_k_count / answerable_count
    ) * 100

    miss_percentage = (
        miss_count / answerable_count
    ) * 100

else:

    rank_1_percentage = 0
    top_k_percentage = 0
    miss_percentage = 0

# Print final results
print("\n" + "=" * 40)
print("=== RETRIEVER EVALUATION ===")
print("=" * 40)

print(f"Answerable questions: {answerable_count}")
print(f"Not answerable questions: {not_answerable_count}")

print(
    f"\nRank 1: {rank_1_count}/{answerable_count} "
    f"({rank_1_percentage:.1f}%)"
)

print(
    f"Top-K:  {top_k_count}/{answerable_count} "
    f"({top_k_percentage:.1f}%)"
)

print(
    f"Miss:   {miss_count}/{answerable_count} "
    f"({miss_percentage:.1f}%)"
)

# Save results
output_path = "evaluation/retriever_results_clean.json"

output_data = {
    "retrieval_k": RETRIEVAL_K,
    "answerable_questions": answerable_count,
    "not_answerable_questions": not_answerable_count,
    "rank_1": rank_1_count,
    "top_k": top_k_count,
    "miss": miss_count,
    "rank_1_percentage": round(rank_1_percentage, 2),
    "top_k_percentage": round(top_k_percentage, 2),
    "miss_percentage": round(miss_percentage, 2),
    "results": results,
}

with open(
    output_path,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        output_data,
        file,
        ensure_ascii=False,
        indent=2,
    )

print(f"\nResults saved to: {output_path}")