



# RAG-Powered Internal Docs Chatbot

A Streamlit-based chatbot for answering queries from internal company documentation (e.g., employee handbooks, policy PDFs) using Retrieval-Augmented Generation (RAG). Powered by FAISS, custom embedding pipelines, and LLMs.

🔗 **Live Demo:** [Try it on Streamlit Cloud](https://rag-app-docs-chatbot-2cjfvaoaedrrubqqc6ydu5.streamlit.app/)

---

## 📁 Project Structure



.
├── .streamlit/              # Streamlit Cloud settings
│   └── config.toml
├── data/                    # Indexed knowledge base and raw documents
│   ├── Employee-Handbook.pdf
│   ├── faiss.index
│   └── chunks.pkl
├── src/                     # Source code
│   ├── app.py               # Streamlit frontend
│   ├── chat\_chain.py        # RAG logic and query pipeline
│   ├── chunk\_and\_embed.py   # Embedding + FAISS indexing
│   └── extract\_text.py      # PDF text extraction logic
├── .env                     # Environment variables (e.g., API keys)
├── requirements.txt         # Python dependencies
├── README.md                # Project overview
└── .gitignore



---

##  Features

- 📄 PDF document ingestion and text chunking
-  Semantic search using FAISS
-  RAG-based LLM querying
-  Streamlit UI for user interaction
-  Modular and extensible Python architecture

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/rag-powered-internal-docs-chatbot.git
cd rag-powered-internal-docs-chatbot
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your `.env` file

Create a `.env` file with your API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Run the app locally

```bash
streamlit run src/app.py
```

---

##  How It Works

1. **Document Parsing**
   `extract_text.py` reads and extracts raw text from PDFs.

2. **Embedding & Indexing**
   `chunk_and_embed.py` splits text into chunks, embeds them via OpenAI embeddings, and stores them in a FAISS index.

3. **Query Handling**
   `chat_chain.py` handles the RAG logic — retrieving similar chunks and prompting the LLM.

4. **UI Layer**
   `app.py` connects everything via Streamlit for user interaction.

---

## 📦 Deployment

Already deployed on **Streamlit Cloud** at:
 [https://rag-app-docs-chatbot-2cjfvaoaedrrubqqc6ydu5.streamlit.app](https://rag-app-docs-chatbot-2cjfvaoaedrrubqqc6ydu5.streamlit.app)

To deploy your own:

1. Push the project to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Set:

   * **Main file path**: `src/app.py`
   * Add `OPENAI_API_KEY` in secrets

---

##  Example Use Cases

* Company internal FAQ bot
* Employee onboarding assistant
* Compliance or HR policy assistant

---

##  Environment Variables

| Variable         | Description                 |
| ---------------- | --------------------------- |
| `OPENAI_API_KEY` | Your OpenAI key for the LLM |

---

## 📄 License

MIT License. See `LICENSE` for more details.

---
```

---

Would you like me to generate this as an actual `README.md` file for direct download or paste it in your folder?
```

