from extract_text import load_pdf
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import pickle

# Load PDF text
pdf_path = "data/Employee-Handbook.pdf"
long_text = load_pdf(pdf_path)

# Split text into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_text(long_text)

# Embed chunks
embedder = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedder.encode(chunks)

# Build and save FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)
faiss.write_index(index, "data/faiss.index")
pickle.dump(chunks, open("data/chunks.pkl", "wb"))

print("✅ Embedding and indexing completed.")