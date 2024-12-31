# #  in this file we have the concepts of the Chain..
# # from langchain import LLMChain
# from langchain_openai import OpenAI
# from langchain_core.prompts import PromptTemplate
# ************************************************************************************************************************************************************
# # # Define Prompt and LLM  Method 1(But due to some classes deprecated it would be giving some warning  )
# template = "What is a good name for a {product} company?"
# prompt = PromptTemplate(input_variables=["product"], template=template)
# llm = OpenAI(temperature=0.7)

# # # Create and Run Chain
# # chain = LLMChain(prompt=prompt, llm=llm)
# # response = chain.run("AI tools")
# # print(response)


# # Create a new runnable chain using the pipe operator
# chain = prompt | llm

# # Run the chain
# response = chain.invoke("AI tools")
# print(response)

# from langchain.prompts import PromptTemplate
# from langchain_openai import OpenAI
# from langchain import LLMChain


# templates = "Translate in hindi: {text}"
# prompt = PromptTemplate(template=templates, input_variables=["text"])


# #  Create the model;
# llm = OpenAI(temperature=0.5)
# #  create the chain..

# chain = LLMChain(llm=llm, prompt=prompt)

# print(chain.run("I'm not go to School"))


# templates = "Translate in hindi: {text}"
# prompt = PromptTemplate(template=templates, input_variables=["text"])

# llm_model = OpenAI(temperature=0.3)

# chain = llm_model | prompt
# print(
#     chain.invoke(
#         {"text": "My name is tushar kumar and I belong to the Uttar Pradesh,Modinagar"}
#     )
# )


# from langchain.prompts import PromptTemplate
# from langchain_openai import OpenAI
# from langchain.chains.llm import LLMChain

# # Define the prompt template
# template = "Translate the following text to Hindi: {text}"
# prompt = PromptTemplate(input_variables=["text"], template=template)

# # Create the LLM (Large Language Model) instance
# llm = OpenAI(temperature=0.7)

# Chain the prompt with the LLM model (using the pipe operator)
# chain = prompt | llm

# # Run the chain to generate the result
# result = chain.invoke("My name is Tushar Kumar")

# # Output the result (translated text)
# print(result)

# chain = LLMChain(prompt=prompt, llm=llm)
# print(chain.run("Hello How are You"))

# *************************************************************************************************************************************************************

#  Simple Sequential Chains i.e the output of the first chain is work as the input for the second chain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain import LLMChain
from langchain.chains.sequential import SimpleSequentialChain

# #  we want to create the multiple chains but step wise step..
# template = "I want to open my {HFT} company, Suggest a Good name for my company"
# llm_model = OpenAI(temperature=0.3)

# prompt = PromptTemplate(template=template, input_variables=["HFT"])
# chain1 = prompt | llm_model

# template2 = (
#     "Suggest the development steps for the {HFT_name}. Return it as a Comma Separated"
# )

# prompt2 = PromptTemplate(template=template2, input_variables=["HFT_name"])
# chain2 = prompt2 | llm_model

# chain = SimpleSequentialChain(chains=[chain1, chain2])

# # Step 4: Run the sequential chain by passing the industry type (e.g., 'HFT')
# output = chain.run({"HFT": "HFT"})  # Input industry as 'HFT'

# # Print the result
# print(output)


# Initialize the OpenAI LLM with a temperature setting
# llm = OpenAI(temperature=0.6)

# # Define the prompt template for generating restaurant names based on cuisine
# prompt_template_name = PromptTemplate(
#     input_variables=["cuisine"],
#     template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this.",
# )

# # Create an LLMChain using the prompt template for restaurant names
# name_chain = prompt_template_name | llm

# # print(name_chain.invoke("Indian"))

# # Define the prompt template for generating menu items based on the restaurant name
# prompt_template_items = PromptTemplate(
#     input_variables=["restaurant_name"],
#     template="""Suggest some menu items for {restaurant_name}. Return it as a comma separated list.""",
# )

# # Create an LLMChain for generating food items based on the restaurant name
# food_items_chain = prompt_template_items | llm

# # Create a SimpleSequentialChain to execute the name chain and then the food items chain
# chain = SimpleSequentialChain(chains=[name_chain, food_items_chain])

# # Run the chain with an input value for cuisine
# response = chain.invoke("Indian")

# # Print the generated response
# print(response)


# template = "What is {name} company and what is the main {work} of it?"
# prompt = PromptTemplate(input_variables=["name", "work"], template=template)
# llm = OpenAI(temperature=0.7)

# chain = prompt | llm

# print(chain.invoke({"name": "HFT", "work": "function"}))


# *************************************************** SIMPLE SEQUENTIAL CHAIN ********************************************************************************
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains.sequential import SequentialChain
from langchain.chains.llm import LLMChain

# Initialize LLM
llm = OpenAI(temperature=0.7)

# Chain 1: Generating a restaurant name
prompt1 = PromptTemplate(
    input_variables=["cuisine"],
    template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this.",
)
# chain1 = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")
chain1 = prompt1 | llm

# Chain 2: Generating menu items based on the restaurant name
prompt2 = PromptTemplate(
    input_variables=["restaurant_name"],
    template="Suggest some menu items for {restaurant_name}.",
)
# chain2 = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")
chain2 = prompt2 | llm

# Sequential Chain: Combine name_chain and food_items_chain
chain = SequentialChain(
    chains=[chain1, chain2],
    input_variables=["cuisine"],
    output_variables=["restaurant_name", "menu_items"],
)

# Run the chain with input cuisine type
response = chain.invoke({"cuisine": "Indian"})  # (Input for the first prompt..)
print(response)
