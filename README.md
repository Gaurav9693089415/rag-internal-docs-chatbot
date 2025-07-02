



 ## RAG-Powered Internal Docs Chatbot

A lightweight chatbot for querying internal documents (e.g., employee handbooks) using **RAG (Retrieval-Augmented Generation)** and **OpenAI GPT-3.5**.

🔗 **Live App:** [Try it on Streamlit →](https://rag-app-docs-chatbot-2cjfvaoaedrrubqqc6ydu5.streamlit.app/)



#  Features 

-  Preloaded internal handbook for instant Q&A
-  Semantic search via FAISS vector similarity
-  GPT-powered answers to employee questions
-  Uses Sentence Transformers + LangChain






## 🗂️ Project Structure
```
rag-internal-docs-chatbot/
│
├── .streamlit/
│ └── config.toml # Streamlit deployment config
│
├── data/
│ ├── Employee-Handbook.pdf # Your input document
│ ├── faiss.index # Vector index
│ └── chunks.pkl # Pickled text chunks
│
├── src/
│ ├── app.py # Streamlit frontend app
│ ├── chat_chain.py # RAG chain logic
│ ├── chunk_and_embed.py # PDF chunking + FAISS indexing
│ └── extract_text.py # Utility to extract text from PDF
│
├── .env # Add your OpenAI API key here (not committed)
├── .gitignore
├── requirements.txt
└── README.md

```

## ⚙️ Setup Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/Gaurav9693089415/rag-internal-docs-chatbot.git
   cd rag-internal-docs-chatbot
```

2. **Create & activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate        # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your OpenAI API key**

   Create a file `src/.env` with:

   ```
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
   ```

5. **Preprocess the document (embedding & indexing)**

   ```bash
   cd src
   python chunk_and_embed.py
   ```

6. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

## 🌐 Deployment on Streamlit Cloud

Already deployed here:
📍 [https://rag-app-docs-chatbot-2cjfvaoaedrrubqqc6ydu5.streamlit.app](https://rag-app-docs-chatbot-2cjfvaoaedrrubqqc6ydu5.streamlit.app)

**To deploy your own version:**

1. Push this repo to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and link your repo
3. Set `OPENAI_API_KEY` using the **Secrets Manager**
4. Done 

---

##  Tech Stack

* [LangChain](https://www.langchain.com/)
* [OpenAI GPT-3.5](https://platform.openai.com/)
* [FAISS](https://github.com/facebookresearch/faiss)
* [HuggingFace Sentence Transformers](https://www.sbert.net/)
* [Streamlit](https://streamlit.io/)

---

##  Use Cases

* Internal policy/document Q\&A
* Employee handbook assistants
* Compliance / onboarding chatbots

---

##  Author

Made by  [Gaurav Kumar](https://github.com/Gaurav9693089415)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE)

```
