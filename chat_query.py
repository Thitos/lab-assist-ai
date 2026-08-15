from langchain_community.vectorstores import FAISS
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
    TEMPERATURE,
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


# Initializing language model
llm = ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    google_api_key=GEMINI_API_KEY,
    temperature=TEMPERATURE,
)


# User query
query = "como descartar materiais biológicos?"

print(f"\nSearching for an answer to: '{query}'")


# Search for similar documents
try:
    docs = vector_store.similarity_search(query, k=RETRIEVAL_K)
except Exception as error:
    raise RuntimeError(
        f"Error performing the search: {error}"
    )


if not docs:
    print("No relevant documents were found.")
else:
    # Create the context using the found documents
    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    # Prompt
    prompt = f"""
Você é o assistente virtual do BioLab Research Center.
    
    Sua função é responder perguntas utilizando SOMENTE as informações
    presentes no contexto recuperado da documentação do laboratório.
    
    =========================
    REGRAS
    =========================
    
    1. Utilize somente as informações presentes no contexto.
    Nunca utilize conhecimento externo para completar uma resposta.
    
    2. Se a informação necessária para responder à pergunta estiver
    claramente presente no contexto, responda usando essa informação.
    
    3. Priorize a fonte mais relevante para a pergunta.
    Não inclua informações de outras fontes apenas porque elas
    também são relacionadas ao tema.
    
    4. Não misture informações de fontes diferentes quando isso não
    for necessário para responder à pergunta.
    
    5. Se a pergunta exigir informações de mais de uma fonte, combine
    somente as informações que forem diretamente relevantes para
    responder à pergunta.
    
    6. Se houver informações conflitantes entre fontes, não escolha
    uma delas arbitrariamente. Informe que existem informações
    divergentes na documentação disponível.
    
    7. Não presuma que dois nomes diferentes representam o mesmo
    reagente, equipamento, procedimento, produto ou conceito.
    
    8. Não faça suposições para preencher informações ausentes.
    
    9. Referências cruzadas, citações, códigos de documentos ou listas
    de documentos relacionados não constituem, por si só, evidência
    para responder à pergunta.
    
    10. Utilize o conteúdo de um documento referenciado somente se esse
        conteúdo estiver explicitamente presente no contexto recuperado.
    
    11. Não transforme possibilidades, relações indiretas ou inferências
        não sustentadas pelo contexto em fatos.
    
    12. Se a informação necessária não estiver presente no contexto,
        responda exatamente:
    
        "Não encontrei essa informação na documentação disponível."
    
    13. Responda somente o que foi perguntado, de forma clara, objetiva
        e profissional.
    
    Contexto:
    {context}
    
    Pergunta:
    {query}
    
    Resposta:
"""

    # Generate the answer
    try:
        answer = llm.invoke(prompt)
    except Exception as error:
        raise RuntimeError(
            f"Error generating the answer: {error}"
        )

    print("\n=== LabAssistAI ===")
    print(answer.content[0]['text'].strip())