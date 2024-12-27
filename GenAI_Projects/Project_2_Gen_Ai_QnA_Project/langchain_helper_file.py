from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAI
from langchain_community.document_loaders import CSVLoader
from langchain.prompts import PromptTemplate
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_openai import OpenAIEmbeddings
import os
from langchain_groq import ChatGroq
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env (especially openai api key

# genai.configure(api_key="AIzaSyDH06uX7C84RldcVLM86TQKuwW22hfwGc8")
# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("write a poem for cryptocurrency")

# Creating the Open ai LLM model.
llm = OpenAI(api_key=os.environ["OPENAI_API"], temperature=0.4, max_tokens=300)

# llm = ChatGroq(
#     model_name="llama-3.1-70B-versatile",
#     temperature=0,
#     groq_api_key="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",
#     max_tokens=300,
# )


# This is the first step in our technical architecture to load the CSV Data..

# Use a pre-trained OpenAI Embeddings. model
openai_embeddings = OpenAIEmbeddings()

vector_file_path = "faiss_index"


def create_vector_database():
    loader = CSVLoader(file_path="predefined_QnA.csv", source_column="prompt")
    data = loader.load()

    # Create FAISS vector store from documents
    vectordb = FAISS.from_documents(documents=data, embedding=openai_embeddings)

    # Optionally: Save the FAISS index to a local file for later use
    vectordb.save_local(vector_file_path)


def get_QNA_chain():
    # Load the vector database from the local folder..
    vectordb = FAISS.load_local(
        vector_file_path, openai_embeddings, allow_dangerous_deserialization=True
    )

    # Create a retriever for querying the vector database..
    retriever = vectordb.as_retriever()

    prompt_template = """Given the following context and a question, generate an detailed answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.
    
    CONTEXT: {context}
    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        input_key="query",
        chain_type_kwargs={"prompt": PROMPT},
    )

    return chain


if __name__ == "__main__":
    chain = get_QNA_chain()

    print(chain("do you provide internship? Do you have EMI Option?"))
