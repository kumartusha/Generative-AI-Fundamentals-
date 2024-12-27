import streamlit as st
from langchain_helper_file import get_QNA_chain, create_vector_database


st.title("GenAI Q&A Support🤝")
btn = st.button("Create Knowledgebase")
if btn:
    create_vector_database()

question = st.text_input("Question: ")

if question:
    chain = get_QNA_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])
