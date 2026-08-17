import streamlit as st

from rag.pipeline import ask_question

st.set_page_config(
    page_title="LabAssistAI",
    page_icon="🧪",
)

st.title("LabAssistAI")

st.subheader(
    "Assistente inteligente para laboratórios de pesquisa"
)

# Conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message.get("sources"):

            st.caption("Fontes consultadas:")

            for source in message["sources"]:
                st.caption(f"• {source}")

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

                    st.caption("Fontes consultadas:")

                    for source in sources:
                        st.caption(
                            f"• {source}"
                        )

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