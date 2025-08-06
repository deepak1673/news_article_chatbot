import os
import time
import pickle
import streamlit as st
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

st.title("News Research Tool")
st.sidebar.title("News Article URLs")

# Collect URLs from user input
urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    if url:
        urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")

file_path = 'faiss_store.pkl'
main_placeholder = st.empty()

# If Process button is clicked
if process_url_clicked and urls:
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data loading... Started...")
    data = loader.load()

    main_placeholder.text("Splitting text into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000,
        chunk_overlap=100
    )
    docs = text_splitter.split_documents(data)

    main_placeholder.text("Creating embedding vector...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)

    with open(file_path, "wb") as f:
        pickle.dump(vectorstore, f)

    main_placeholder.success("Processing complete!")

# Ask a question after processing
query = st.text_input("Ask a question about the news articles:")

if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vector_store = pickle.load(f)

        retriever = vector_store.as_retriever()

        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0.6,
            google_api_key=api_key
        )

        chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            return_source_documents=True
        )

        result = chain({"query": query})

        st.header("Answer")
        st.write(result["result"])

        st.subheader("Source Documents")
        for i, doc in enumerate(result["source_documents"]):
            st.write(f"Source {i+1}: {doc.metadata.get('source', 'Unknown')}")
            st.write(doc.page_content[:300] + "...")
    else:
        st.error("Please process the URLs first.")
