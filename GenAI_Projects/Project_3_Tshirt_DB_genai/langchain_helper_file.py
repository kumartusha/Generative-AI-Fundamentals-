from langchain_community.llms import GooglePalm
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import Chroma
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import OpenAI
from few_shots_learning import few_shots
from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI

import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env (especially openai api key)

# llm = GooglePalm(google_api_key = os.environ["GOOGLE_API_KEY"], temperature = 0.2)


def get_few_shot_db_chain():
    db_user = "root"
    db_password = "1234!%40%23%24Tushar"
    db_host = "localhost"
    db_name = "llm_tshirt_store"

    db = SQLDatabase.from_uri(
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
        sample_rows_in_table_info=3,
    )

    print(db.table_info)
    # llm = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.1)

    llm = OpenAI(temperature=0.4, api_key=os.environ["OPEN_AI_API"])

    embeddings_openai = OpenAIEmbeddings()

    vector_string_db = [" ".join(map(str, example.values())) for example in few_shots]

    # try:
    # Manually process metadata
    simplified_metadata = []
    for item in few_shots:
        processed_item = {
            key: str(value) for key, value in item.items()
        }  # Convert all values to strings
        simplified_metadata.append(processed_item)

        # Pass the simplified metadata to Chroma
    vectorstores = Chroma.from_texts(
        vector_string_db, embeddings_openai, metadatas=simplified_metadata
    )
    #     print(type(vectorstores))
    # except Exception as e:
    #     print(f"Error: {e}")

    example_selector = SemanticSimilarityExampleSelector(vectorstore=vectorstores, k=2)

    mysql_prompt = """You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use CURDATE() function to get the current date, if the question involves "today".

    Use the following format:

    Question: Question here
    SQLQuery: Query to run with no pre-amble
    SQLResult: Result of the SQLQuery
    Answer: Final answer here

    No pre-amble.
    """

    example_prompt = PromptTemplate(
        input_variables=[
            "Question",
            "SQLQuery",
            "SQLResult",
            "Answer",
        ],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=[
            "input",
            "table_info",
            "top_k",
        ],  # These variables are used in the prefix and suffix
    )

    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt)
    return chain


if __name__ == "__main__":
    chain = get_few_shot_db_chain()
    # ans = chain.run("How many total tshirt are left in total in stock")
    # print(ans)
