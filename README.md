Here's your `README.md` written in **screenshot style**, exactly how it appears in the image format you're aiming for:

---

```markdown
#  RAG-Powered Internal Docs Chatbot

A lightweight chatbot for querying internal documents (e.g., employee handbooks) using **RAG (Retrieval-Augmented Generation)** and **OpenAI GPT-3.5**.

🔗 **Live App:** [Try it on Streamlit →](https://rag-app-docs-chatbot-2cjfvaoaedrrubqqc6ydu5.streamlit.app/)

---

##  Features

-  Preloaded internal handbook for instant Q&A  
-  Semantic search via FAISS vector similarity  
-  GPT-powered answers to employee questions  
-  Uses Sentence Transformers + LangChain  

---

## 🗂️ Project Structure

```

rag-internal-docs-chatbot/
│
├── .streamlit/
│   └── config.toml             # Streamlit deployment config
│
├── data/
│   ├── Employee-Handbook.pdf   # Your input document
│   ├── faiss.index             # Vector index
│   └── chunks.pkl              # Pickled text chunks
│
├── src/
│   ├── app.py                  # Streamlit frontend app
│   ├── chat\_chain.py           # RAG chain logic
│   ├── chunk\_and\_embed.py      # PDF chunking + FAISS indexing
│   └── extract\_text.py         # Utility to extract text from PDF
│
├── .env                        # Add your OpenAI API key here (not committed)
├── .gitignore
├── requirements.txt
└── README.md

````

---

## ⚙️ Setup Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/Gaurav9693089415/rag-internal-docs-chatbot.git
   cd rag-internal-docs-chatbot
````

2. **Create virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set your API key**
   Create a `.env` file inside `src/` and add:

   ```
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
   ```

5. **Run the app**

   ```bash
   streamlit run src/app.py
   ```

---

##  Deployment on Streamlit Cloud

Already deployed here: [https://rag-app-docs-chatbot-2cjfvaoaedrrubqqc6ydu5.streamlit.app](https://rag-app-docs-chatbot-2cjfvaoaedrrubqqc6ydu5.streamlit.app)

To deploy your own version:

1. Push this repo to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and link your repo
3. Set `OPENAI_API_KEY` using the **Secrets Manager**
4. Done 

---

## 🙋‍♂️ Author

**Gaurav Kumar**
[GitHub](https://github.com/Gaurav9693089415) • [LinkedIn](https://www.linkedin.com/in/gaurav9693089415)

