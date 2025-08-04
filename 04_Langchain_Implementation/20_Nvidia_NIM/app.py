from langchain_nvidia_ai_endpoints import ChatNVIDIA,NVIDIAEmbeddings
import os
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
import time
import streamlit as st

from dotenv import load_dotenv

load_dotenv()

os.environ['NVIDIA_API_KEY']=os.getenv('NVIDIA_API_KEY')

def vector_embedding():
  
  if "vectors" not in st.session_state:
    st.session_state.embeddings=NVIDIAEmbeddings()
    st.session_state.loader=PyPDFDirectoryLoader("./us_census")
    st.session_state.docs=st.session_state.loader.load()
    st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=700,chunk_overlap=50)
    st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs)
    st.session_state.vectors=FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings)

st.title("PDF Query || LLM Infernce with Nvidia NIM")
llm=ChatNVIDIA( model="meta/llama-3.2-1b-instruct",temperature=0.2,
  top_p=0.7,
  max_tokens=1024)

prompt=ChatPromptTemplate.from_template(
  """
  Answer the questions based on the provided context only.
  please provide the most accurate response based on thr question and context provided.
  <context>
  {context}
  <context>
  Questions::{input}
  """
)

user_input=st.text_input("Enter Your Question Related to Documents..")

if st.button("Documents Embedding"):
    vector_embedding()
    st.write("Vector Store DB Is Ready")


if user_input:
  document_chain=create_stuff_documents_chain(llm,prompt)
  retriever=st.session_state.vectors.as_retriever()
  retriever_chain=create_retrieval_chain(retriever,document_chain)
  start=time.process_time()
  response=retriever_chain.invoke({'input':user_input})
  print("Response time :",time.process_time()-start)
  
  st.write(response['answer'])
  
  with st.expander("Document Similarity Search"):
    for i,docs in enumerate(response["context"]):
      st.write(docs.page_content)
      st.write("____________**********_______________")


  
