import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains_file import Chain
from portfolio_file import Portfolio
from utils_files import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 AI-Driven Cold Email Generator")
    url_input = st.text_input(
        "Enter a URL:", value="https://www.atlassian.com/company/careers/details/17052"
    )
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(
                loader.load().pop().page_content
            )  # Here we have the scrapped web data

            portfolio.load_portfolio()  # Create Chroma DB
            jobs = llm.extract_jobs(data)

            # st.write(jobs)
            for job in jobs:
                skills = job.get("skills", [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                # st.write(email)
                st.code(email, language="markdown")
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)
    # print("All working")
