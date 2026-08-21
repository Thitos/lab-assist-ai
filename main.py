import streamlit as st

from rag.pipeline import ask_question
from get_knowledge_base import get_knowledge_base
from config import CATEGORY_LABELS

st.set_page_config(
    page_title="LabAssistAI",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar
knowledge_base = get_knowledge_base()
with st.sidebar:

    st.markdown("## 🧪 LabAssistAI")

    st.caption(
        "Assistente inteligente para laboratórios de pesquisa"
    )

    st.divider()

    st.markdown("### Sobre")

    st.write(
        "Consulte protocolos, equipamentos, estoque e "
        "documentação institucional utilizando linguagem natural."
    )

    # Knowledge Base
    st.markdown("### 📚 Base de conhecimento")

    for category, documents in knowledge_base.items():
        label = CATEGORY_LABELS[category]
        with st.expander(f"{label} ({len(documents)})"):
            for document in documents:
                st.markdown(
                    f"**{document['id']}**  \n"
                    f"{document['title']}"
                )

    st.divider()

    st.markdown("### Tecnologias")

    st.markdown(
        """
        - 🐍 Python
        - 🧠 Google Gemini
        - 🔎 Gemini Embeddings
        - 🗄️ FAISS
        - 🔗 LangChain
        - ⚡ Streamlit
        """
    )

    st.divider()

    st.caption("BioLab Research Center")
    st.caption("RAG Assistant • Demo")

# Main header
st.title("🧪 LabAssistAI")

st.subheader(
    "Assistente inteligente para laboratórios de pesquisa"
)

# Conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Welcome message
if not st.session_state.messages:

    st.markdown(
        "### Como posso ajudar?"
    )

    st.write(
        "Consulte a documentação do laboratório em linguagem natural. "
        "Você pode perguntar sobre protocolos, equipamentos, estoque, "
        "biossegurança e procedimentos administrativos."
    )

    st.info(
        "💡 Exemplos: "
        "Quem é o responsável pelo laboratório?  "
        "Tenho no estoque todos os reagentes para extrair RNA?  "
        "Quais são as configurações do termociclador para qPCR?"
    )

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message.get("sources"):

            with st.expander(
                f"📚 Fontes consultadas ({len(message['sources'])})"
            ):

                for source in message["sources"]:
                    st.markdown(f"- `{source}`")

# Chat input
query = st.chat_input(
    "Digite a sua pergunta..."
)

if query:

    # Display user question
    with st.chat_message("user"):
        st.markdown(query)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": query,
    })

    # Generate answer
    with st.chat_message("assistant"):

        with st.spinner("Consultando a documentação..."):

            try:

                result = ask_question(query)

                answer = result["answer"]
                sources = result["sources"]

                st.markdown(answer)

                if sources:

                    with st.expander(
                        f"📚 Fontes consultadas ({len(sources)})"
                    ):

                        for source in sources:
                            st.markdown(f"- `{source}`")

                else:

                    st.caption(
                        "Nenhuma fonte encontrada."
                    )

                # Save assistant response
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "sources": sources,
                })

            except Exception as error:

                error_message = str(error)

                # API limit/quota error
                if (
                    "429" in error_message
                    or "RESOURCE_EXHAUSTED" in error_message
                    or "quota" in error_message.lower()
                ):

                    friendly_message = (
                        "⏳ O LabAssistAI está temporariamente indisponível devido "
                        "à alta demanda.\n\n"
                        "Por favor, aguarde alguns segundos e tente "
                        "novamente."
                    )

                else:

                    friendly_message = (
                        "⚠️ Não foi possível processar sua pergunta "
                        "neste momento.\n\n"
                        "Tente novamente em instantes."
                    )

                st.warning(friendly_message)

                # Log the error only to the terminal/log
                print(f"Erro no processamento: {error}")