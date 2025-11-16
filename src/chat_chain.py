from langchain_openai import ChatOpenAI  

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chains import RetrievalQA
from langchain.docstore import InMemoryDocstore
from langchain.schema import Document

import faiss
import pickle
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Load index and chunks
index = faiss.read_index("data/faiss.index")
chunks = pickle.load(open("data/chunks.pkl", "rb"))

# Wrap chunks in Document objects
documents = {str(i): Document(page_content=chunks[i]) for i in range(len(chunks))}
docstore = InMemoryDocstore(documents)
index_to_docstore_id = {i: str(i) for i in range(len(chunks))}

# Embedder and Vectorstore
embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS(
    embedding_function=embedder,
    index=index,
    docstore=docstore,
    index_to_docstore_id=index_to_docstore_id
)

# LLM and Retrieval Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-3.5-turbo", api_key=api_key),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

def answer_query(query: str):
    return qa_chain.run(query)
