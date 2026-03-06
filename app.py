import streamlit as st
from rag_pipeline import process_pdf, ask_question

st.title("NotebookLM Clone")

uploaded_file = st.file_uploader("Upload PDF")

if uploaded_file:

    with open("temp.pdf","wb") as f:
        f.write(uploaded_file.read())

    process_pdf("temp.pdf")

    st.success("PDF processed successfully")

question = st.text_input("Ask a question")

if question:

    answer = ask_question(question)

    st.write(answer)