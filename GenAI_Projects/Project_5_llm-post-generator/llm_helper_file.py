from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

#  This command is used to the the api key as a environment variable..
load_dotenv()

llm = ChatGroq(api_key=os.environ["GROQ_API_KEY"], model="Llama-3.3-70b-Specdec")

if __name__ == "__main__":
    print(llm.invoke("Who is the founder of the BlackRock").content)
