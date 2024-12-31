#  How to use the Open ai llm model.
from langchain_openai import OpenAI
import streamlit as st


# import os
# print(os.getenv("OPENAI_API_KEY"))
# llm = OpenAI(temperature=0.2, max_tokens=300)
# print(llm.invoke("what is the networth of the rihana singer"))

#  FIrst
# llm = OpenAI(temperature=0.2, max_tokens=300)
# response = llm.invoke("Who is Elon Musk? proper structured format 1000 words")
# print(response)

#  Second
llm = OpenAI(temperature=0.7, max_tokens=500)
# response = llm.invoke(
#     "hat kind of bitcoin solved the problem and in future is there any other technology comes like the bitcoin"
# )
# print(response)

# #  Third
# response = llm.generate(
#     prompt="What are the latest trends in artificial intelligence?",
#     max_tokens=500,
#     temperature=0.3,
# )
# print(response)

# #  Fourth
# question = st.text_input("What's Comes in your mind just type below ??")
# response = llm.stream(question)

# if st.button("Process"):
#     # for chunk in response:
#     st.write(response)

# #  Fifth
# responses = llm.generate(
#     prompts=["Give me a list of top programming languages in 2024."],
#     num_completions=3,
#     max_tokens=100,
# )

# print(responses)
# for i, response in enumerate(responses):
#     print(f"Response {i+1}: {response}")
