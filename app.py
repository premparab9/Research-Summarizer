
import streamlit as st
import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
EMBED_MODEL = os.getenv("EMBEDDING_MODEL")


st.title("AI Research Paper Summarizer")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    os.makedirs("data", exist_ok=True)
    file_path = "data/temp.pdf"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    loader = PyPDFLoader(file_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    split_docs = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings(
        model=EMBED_MODEL,
        base_url=BASE_URL,
        api_key=API_KEY
    )

    db = FAISS.from_documents(split_docs, embeddings)


    llm = ChatOpenAI(
        model=MODEL_NAME,
        base_url=BASE_URL,
        api_key=API_KEY,
        temperature=0
    )

    if st.button("Generate Summary"):
        text = " ".join([doc.page_content for doc in split_docs[:5]])

        prompt = f"""
        Summarize this research paper in simple terms:

        {text}
        """

        result = llm.invoke(prompt)
        st.write(result.content)

    query = st.text_input("Ask question about paper:")

    if query:
        retrieved_docs = db.similarity_search(query, k=3)
        context = " ".join([doc.page_content for doc in retrieved_docs])

        prompt = f"""
        Answer ONLY from the context below.
        If not found, say "Not in paper".

        Context:
        {context}

        Question:
        {query}
        """
        result = llm.invoke(prompt)
        st.write(result.content)
