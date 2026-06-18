import streamlit as st

from utils.pdf_loader import load_pdf_text
from utils.text_splitter import split_text_into_chunks
from utils.vector_store import create_vector_store
from utils.qa_chain import get_llm


st.set_page_config(
    page_title="PDF Chatbot",
    page_icon="📄"
)

st.title("📄 Conversational PDF Chatbot")

# SESSION STATE
# =============================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "memory" not in st.session_state:
    st.session_state.memory = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

# PDF Upload
# =============================

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)


if uploaded_file is not None:

    with st.spinner("Reading PDF..."):

        text = load_pdf_text(uploaded_file)

        chunks = split_text_into_chunks(text)

        vector_store = create_vector_store(chunks)

        st.session_state.vector_store = vector_store
        st.success("PDF processed successfully!")

# DISPLAY CHAT HISTORY
# =============================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# USER INPUT
# =============================

user_question = st.chat_input(
    "Ask question from PDF"
)


if user_question:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )
    with st.chat_message("user"):
        st.markdown(user_question)


    # =============================
    # RETRIEVE DOCUMENTS
    # =============================

    docs = st.session_state.vector_store.similarity_search(
        user_question,
        k=3
    )
    # CREATE CONTEXT
    # =============================

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    # MEMORY WINDOW
    # =============================

    memory_window = st.session_state.memory[-4:]


    conversation_history = ""

    for item in memory_window:

        conversation_history += (
            f"User: {item['question']}\n"
            f"Assistant: {item['answer']}\n"
        )

        # FINAL PROMPT
    # =============================

    prompt = f"""
You are a helpful AI assistant.

Use:
1. Previous conversation history
2. Retrieved PDF context

to answer the question.

====================
Conversation History:
{conversation_history}
====================
PDF Context:
{context}

====================
Current Question:
{user_question}
====================

Answer clearly and briefly.
"""
    # LLM RESPONSE
    # =============================

    llm = get_llm()

    response = llm.invoke(prompt)


    # =============================
    # DISPLAY RESPONSE
    # =============================

    with st.chat_message("assistant"):
        st.markdown(response)

    # STORE CHAT HISTORY
    # =============================

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    # STORE MEMORY
    # =============================

    st.session_state.memory.append(
        {
            "question": user_question,
            "answer": response
        }
    )    