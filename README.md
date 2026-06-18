# 📄 PDF Chatbot using RAG and LangChain

## Overview

This project is a Conversational PDF Chatbot that allows users to upload a PDF document and ask questions about its content.

The chatbot uses Retrieval-Augmented Generation (RAG), LangChain, FAISS, and OpenAI to retrieve relevant information from the document and generate accurate responses.

---

## Features

* Upload PDF documents
* Ask questions about PDF content
* Conversational chat interface
* Semantic search using FAISS
* Context-aware responses using OpenAI
* Memory-based conversation history
* Interactive Streamlit application

---

## Technologies Used

* Python
* Streamlit
* LangChain
* OpenAI
* FAISS
* PyPDF
* Python Dotenv

---

## Project Structure

```text
pdf-chatbot-rag-llm/
│
├── app.py
├── requirements.txt
├── README.md
│
└── utils/
    ├── pdf_loader.py
    ├── text_splitter.py
    ├── vector_store.py
    └── qa_chain.py
```

---

## How It Works

1. Upload a PDF file.
2. Extract text from the PDF.
3. Split text into smaller chunks.
4. Convert chunks into embeddings.
5. Store embeddings in FAISS.
6. Retrieve relevant content based on the user's question.
7. Generate answers using OpenAI.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/pdf-chatbot-rag-llm.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

---

## Skills Demonstrated

* Generative AI
* Retrieval-Augmented Generation (RAG)
* LangChain
* Vector Databases (FAISS)
* OpenAI API Integration
* Prompt Engineering
* Streamlit Development

---

## Future Improvements

* Multi-PDF support
* Source citations
* Chat history export
* Local LLM integration

---

## Author

**Tejaswini Narra**

Aspiring AI & Machine Learning Engineer
