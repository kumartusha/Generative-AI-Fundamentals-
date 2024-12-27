import os
import streamlit as st
import time

# from langchain import OpenAI
from langchain_openai import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()  # Take environment variables from .env (especially openai api key)

st.title("SmartBot: News Research Tool 📈")
st.sidebar.title("News Article URLs")

# Collect URLs from the sidebar
urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    print(url)
    print()
    urls.append(url)


process_url_clicked = st.sidebar.button("Process URLs")
faiss_index_path = "faiss_index"  # Directory to save the FAISS index

#  Above the question input.
main_placeholder = st.empty()

# Define the embeddings model once
embeddings = OpenAIEmbeddings()

#  Create the instance of the LLM Model
llm = OpenAI(temperature=0.4, max_tokens=500)

if process_url_clicked:
    # Ensure at least one URL is provided
    if not any(urls):
        st.sidebar.error("Please provide at least one URL.")
        st.stop()

    # Load data from URLs
    loader = UnstructuredURLLoader(urls=urls)

    try:
        main_placeholder.text("Data Loading...Started...✅✅✅")
        data = loader.load()
        # Log the data to check if it's loaded properly
        # st.write(f"Loaded data: {data}")
    except Exception as e:
        st.sidebar.error(f"Error loading data: {e}")
        st.stop()

    # Check if data is empty
    if not data:
        st.sidebar.error("No data was loaded from the provided URLs.")
        st.stop()

    # Split the data into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", ","], chunk_size=1000
    )
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs = text_splitter.split_documents(data)

    # Ensure there are documents to process
    if not docs:
        st.sidebar.error("No documents found after processing the URLs.")
        st.stop()

    # Create embeddings and store in FAISS index
    try:
        vectorstore_openai = FAISS.from_documents(docs, embeddings)
        main_placeholder.text("Embedding Vector Started Building...✅✅✅")
        # if vectorstore_openai.is_empty():
        #     st.sidebar.error("FAISS index is empty, unable to save.")
        #     st.stop()
    except Exception as e:
        st.sidebar.error(f"Error creating FAISS vector store: {e}")
        st.stop()

    # Save the FAISS index locally
    try:
        vectorstore_openai.save_local(faiss_index_path)
        st.sidebar.success("FAISS index saved successfully!")
    except Exception as e:
        st.sidebar.error(f"Error saving FAISS index: {e}")
        st.stop()

query = main_placeholder.text_input("Question: ")

print(query)
if query:

    # Load the FAISS index from local storage
    if os.path.exists(faiss_index_path):
        try:
            loaded_vectorstore_openai = FAISS.load_local(
                faiss_index_path,
                embeddings,  # Make sure the same embeddings model is used
                allow_dangerous_deserialization=True,  # Allow dangerous deserialization
            )
            st.sidebar.success("FAISS index successfully loaded!")
        except Exception as e:
            st.sidebar.error(f"Error loading the FAISS index: {e}")
            st.stop()

        # Perform query using the loaded vector store
        chain = RetrievalQAWithSourcesChain.from_llm(
            llm=llm, retriever=loaded_vectorstore_openai.as_retriever()
        )
        #  Result is a dictionary that contain the answer and
        result = chain({"question": query}, return_only_outputs=True)

        st.write(result)

        if "answer" in result:
            st.header("Answer")
            st.write(result["answer"])
        else:
            st.write("No answer found.")

        sources = result.get("sources", "")

        if sources:
            st.subheader("Sources")
            sources_list = sources.split("\n")
            for source in sources_list:
                st.write(source)
    else:
        st.sidebar.error("FAISS index not found at the specified path.")


# # Some Bugs We need to fixed into this project..
