import streamlit as st
import os
from chat_chain import answer_query  # Your function that uses LLM

# Page Configuration
st.set_page_config(page_title="AI Internal Docs Assistant", layout="centered")

# Custom Styling
st.markdown("""
    <style>
        body {
            background-color: #121212;
        }
        .main-title {
            font-size: 2.5em;
            font-weight: 700;
            color: #1e90ff;
            text-align: center;
            margin-bottom: 0.2em;
        }
        .subtitle {
            font-size: 1.3em;
            color: red;
            text-align: center;
            margin-bottom: 2em;
        }
        .about-section {
            background-color: #1a1a1a;
            padding: 1.2em;
            border-radius: 10px;
            color: yellow;
            font-size: 0.95em;
            margin-top: 2em;
        }
        .stChatInput > div {
            background-color: #f0f0f0;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Subtitle
st.markdown('<div class="main-title">AI Internal Docs Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask anything about your company handbook</div>', unsafe_allow_html=True)

# Load Employee Handbook
pdf_path = "data/Employee-Handbook.pdf"
if os.path.exists(pdf_path):
    st.success("Employee Handbook loaded from data folder.")
else:
    uploaded = st.file_uploader("Upload your Employee Handbook", type=["pdf", "docx"])
    if uploaded:
        os.makedirs("data", exist_ok=True)
        with open(pdf_path, "wb") as f:
            f.write(uploaded.read())
        st.success("File uploaded and saved!")

# Initialize session state for messages and chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Clear chat option
if st.button("🗑️ Clear Chat"):
    st.session_state["messages"] = []
    st.session_state["chat_history"] = []
    st.experimental_rerun()

# Display chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
query = st.chat_input("Ask your question here...")

if query:
    # Show user message
    with st.chat_message("user"):
        st.markdown(query)
    st.session_state["messages"].append({"role": "user", "content": query})
    st.session_state["chat_history"].append({"role": "user", "content": query})

    # Build history context (last 5 messages)
    history = [msg["content"] for msg in st.session_state["chat_history"][-5:]]
    query_with_context = "\n".join(history)

    # Get assistant response
    response = answer_query(query_with_context)

    # Show assistant message
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.session_state["chat_history"].append({"role": "assistant", "content": response})

