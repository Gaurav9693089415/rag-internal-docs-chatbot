import streamlit as st
from chat_chain import answer_query

import os

st.title("📄 AI Internal Docs Assistant")

pdf_path = "data/Employee-Handbook.pdf"

if os.path.exists(pdf_path):
    st.success("Employee Handbook loaded from data folder.")
else:
    uploaded = st.file_uploader("Upload a PDF or Doc", type=["pdf"])
    if uploaded:
        with open(pdf_path, "wb") as f:
            f.write(uploaded.getbuffer())
        st.success("Document uploaded and saved!")

query = st.text_input("Ask a question about your documents:")
if query:
    answer = answer_query(query)
    st.write(answer)