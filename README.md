# Research-Summarizer
# 📄 AI Research Paper Summarizer

A simple AI-powered web app that allows users to upload research papers (PDFs) and:
- Generate summaries
- Ask questions about the paper

Built using LangChain, Streamlit, and OpenAI-compatible APIs.

---

## 🚀 Features

- 📄 Upload research papers (PDF)
- 🧠 Generate easy-to-understand summaries
- 💬 Ask questions from the paper (Q&A)
- ⚡ Fast retrieval using vector search (FAISS)
- 🔍 Context-based answers (RAG approach)

---

## 🧠 How it works

1. PDF is loaded and text is extracted  
2. Text is split into smaller chunks  
3. Chunks are converted into embeddings  
4. Stored in FAISS vector database  
5. User query → relevant chunks retrieved  
6. LLM generates answer based on context  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- LangChain  
- FAISS (Vector Database)  
- OpenAI-compatible API (LLM + Embeddings)  

---

## 📁 Project Structure

ai-research-summarizer/
│
├── app.py
├── .env
├── requirements.txt
└── data/


---

## 🔐 Environment Setup

Create a `.env` file in the root folder:
OPENAI_API_KEY=your_api_key
OPENAI_BASE_URL=your_base_url

MODEL_NAME=gpt-35-turbo-16k-france-1
EMBEDDING_MODEL=text-embedding-bge-m3


---

## ▶️ Installation & Run

```bash
# Create virtual environment
python -m venv .venv

# Activate environment
.venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

👨‍💻 Author

Prem Parab
