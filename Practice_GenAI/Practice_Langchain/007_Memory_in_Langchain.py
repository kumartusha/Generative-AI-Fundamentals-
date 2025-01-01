# #  Here in this file we are going to read about the Memory into the Langchain..
# from langchain.chains.conversation.base import ConversationChain
# from langchain.memory import ConversationBufferMemory
# from langchain_openai import OpenAI

# memory = ConversationBufferMemory()
# conversation = ConversationChain(llm=OpenAI(temperature=0), memory=memory)

# print(conversation.invoke("Hello!"))
# print(conversation.invoke("What did I just say?"))


#  Using the  RunnableWithMessageHistory   class with the Langchain..***************************************************************************************
# from langchain.memory import ConversationBufferMemory
# from langchain_openai import OpenAI
# from langchain_core.runnables.history import RunnableWithMessageHistory

# # Initialize memory
# memory = ConversationBufferMemory()

# # Initialize LLM with OpenAI API (use OpenAI model from langchain)
# llm = OpenAI(temperature=0)

# # Create the RunnableWithMessageHistory object to manage conversation
# conversation = RunnableWithMessageHistory(llm=llm, memory=memory)

# # Invoke conversation
# print(conversation.invoke("Hello!"))
# print(conversation.invoke("What did I just say?"))


#  Conversational Chain with the Langchain...........................
# from langchain.memory import ConversationBufferMemory
# from langchain_openai import OpenAI
# from langchain.chains.conversation.base import ConversationChain

# # Initialize memory
# memory = ConversationBufferMemory()

# # Initialize LLM with OpenAI API (use OpenAI model from langchain)
# llm = OpenAI(temperature=0)

# # Create the ConversationalChain object
# conversation = ConversationChain(llm=llm, memory=memory)

# # Simulate conversation
# print(conversation.run("Hello My name is Tushar Kumar"))
# print(conversation.run("I'm a Final Year B.Tech Student"))
# print(conversation.run("What did I just say all previously?"))


#  Ask the Question to the LLM and save the history by using the some different type of memory..
# from langchain.memory import ConversationBufferMemory
# from langchain_openai import OpenAI

# # ----------- ConversationBufferMemory Section -----------
# print("ConversationBufferMemory:")
# memory_buffer = ConversationBufferMemory(
#     memory_key="chat_history", return_messages=True
# )

# # Initialize LLM with ConversationBufferMemory
# llm_buffer = OpenAI(temperature=0)

# # Simulate conversation
# llm_buffer.invoke("Hello, how are you?")
# llm_buffer.invoke("I'm doing great, thank you!")

# # Get and print the entire conversation history
# conversation_history = memory_buffer.load_memory_variables({})["chat_history"]
# print(conversation_history)
# print("--------------------------------------------------")

# ----------- ConversationSummaryMemory Section -----------
# from langchain.memory import ConversationSummaryMemory
# from langchain_openai import OpenAI
# from langchain.chains.conversation.base import ConversationChain

# llm = OpenAI(temperature=0)
# # Initialize memory (using ConversationSummaryMemory)
# memory = ConversationSummaryMemory(
#     llm=llm,
#     memory_key="history",  # The key under which conversation history will be stored
#     human_prefix="Human",  # Prefix for the human's messages
#     ai_prefix="AI",  # Prefix for the AI's responses
# )

# # Initialize LLM with OpenAI API using a newer model (gpt-3.5-turbo

# # Create the ConversationalChain object
# conversation = ConversationChain(llm=llm, memory=memory)

# # Simulate conversation
# print(conversation.invoke("Hello!"))
# print(conversation.invoke("What did I just say?"))
# summary_memory = memory.load_memory_variables({})["history"]
# print(summary_memory)


# # ----------- TokenBufferMemory Section -----------
# print("TokenBufferMemory:")
memory_token = TokenBufferMemory(max_tokens=1000, memory_key="chat_tokens")

# Initialize LLM with TokenBufferMemory
llm_token = OpenAI(model="text-davinci-003", memory=memory_token)

# Simulate conversation
llm_token("Hello, how are you?")
llm_token("I'm doing great, thank you!")

# Get and print the token memory
token_memory = memory_token.load_memory_variables({})["chat_tokens"]
print(token_memory)
# print("--------------------------------------------------")
