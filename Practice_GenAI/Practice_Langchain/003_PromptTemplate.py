# 1. Prompts
# Prompts are templates that structure the input for the LLM. They are central to crafting effective interactions.

# Key Concepts
# Static Prompts: Fixed templates with no dynamic inputs.
# Dynamic Prompts: Templates that take variables as input.
# Example
# python


from langchain_core.prompts import PromptTemplate
import json


# templates = "My name is {name}, and I'm a final Year {course} and I want to become the {profession}"
# prompt = PromptTemplate(
#     input_variables=["name", "course", "profession"], template=templates
# )

# print(prompt.format(name="Tushar Kumar", course="B.Tech", profession="AI/ML Engineer"))


#  ith the Dummy Json Data..
# dummyJson = PromptTemplate.load()
# with open("./dummy.json", "r") as file:
#     dummyData = json.load(file)

# print(dummyData)
# with open("dummy.json", "r") as file:
#     dummyData = json.load(file)

# print(dummyData)
#  Basic Prompt Template..
# templates = "Hello my name is {name} Kumar and my age is {age}"
# # print(
# #     PromptTemplate(input_variables=["name"], template=templates).format(
# #         name="Tushar", age=20
# #     )
# # )
# prompt = PromptTemplate(input_variables=["name"], template=templates)
# print(prompt)
# print(templates)
# print(templates.format(name="Tushar", age=20))

#  Prompt template with the Few Shot Prompt Template..
few_shot_prompt = """
Here are some examples of polite instructions:

Example 1: 
User: Alice
Action: submit the report
Polite Instruction: "Dear Alice, please submit the report as soon as possible."

Example 2:
User: Bob
Action: review the document
Polite Instruction: "Dear Bob, please review the document as soon as possible."

Example 3:
User: Charlie
Action: attend the meeting
Polite Instruction: "Dear Charlie, please attend the meeting as soon as possible."

Now, based on this pattern, please generate a polite instruction for the following:

User: {user}
Action: {action}

Polite Instruction: "Dear {user}, please {action} as soon as possible."
"""


# print(
#     PromptTemplate(input_variables=["user", "action"]).format(
#         user="Tushar Kumar", action="Build the AI/ML Application"
#     )
# )
# print(few_shot_prompt.format(user="Tushar Kumar", action="Develop AI/ML Application"))


# Few-Shot Prompt:
# Dear Alice, please submit the report.
# Dear Bob, please review the document.

# Now, please generate a polite instruction for:
# Dear Tushar, please prepare the presentation.
#  we need to find this output from the dummy.json file and get the output like this..

#  1.Step is to get the data from the json file.

# with open("dummy.json", "r") as file:
#     data = json.load(file)


# examples = data["examples"]
# template = data["template"]

# mod_examples = [
#     template.format(user=example["user"], action=example["action"])
#     for example in examples
# ]
# result = "\n".join(mod_examples)
# print(result)


# from langchain import PromptTemplate

# template = "Translate the following text to French: {text}"
# prompt = PromptTemplate(input_variables=["text"], template=template)

# print(prompt.format(text="Hello, how are you?"))
# print(template.format(text="Hello, how are you?"))


# from langchain import PromptTemplate

# # prompt = PromptTemplate(
# #     input_variables=["text"], template="Translate the following text to French: {text}"
# # )

# template = "Translate the following text to French: {text}"

# # Reusing the same prompt in different parts of the system
# print(template.format(text="Hello"))  # First use
# print(template.format(text="How are you?"))  # Second use


# Chaining example in LangChain (conceptual)
prompt1 = PromptTemplate(
    input_variables=["text"], template="Translate the following text to French: {text}"
)
prompt2 = PromptTemplate(
    input_variables=["text"], template="Summarize the following text: {text}"
)

# Pass the output of one prompt to the next
result = prompt2.format(text=prompt1.format(text="Hello"))
print(result)
