import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFaceHub
from langchain.chains import ConversationalRetrievalChain

st.set_page_config(page_title="Farm-GPT", page_icon="🌾")
st.title("🌾 Farm-GPT: Ask Your Farming Questions")
st.write("Upload farming PDFs and ask questions")

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
llm = HuggingFaceHub(repo_id="mistralai/Mistral-7B-Instruct-v0.1")
