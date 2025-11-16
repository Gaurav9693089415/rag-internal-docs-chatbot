from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_core.prompts import PromptTemplate
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

# Vectorstore
embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS(
    embedding_function=embedder,
    index=index,
    docstore=docstore,
    index_to_docstore_id=index_to_docstore_id
)

retriever = vectorstore.as_retriever()

# LLM
llm = ChatOpenAI(model_name="gpt-3.5-turbo", api_key=api_key)

# Prompt
prompt = PromptTemplate.from_template("""
Use ONLY the context below to answer the question.

Context:
{context}

Question:
{query}

Answer:
""")

def answer_query(query: str):
    docs = retriever.get_relevant_documents(query)
    context = "\n\n".join([doc.page_content for doc in docs])
    formatted_prompt = prompt.format(context=context, query=query)

    response = llm.invoke(formatted_prompt)
    return response.content
