from langchain.agents import AgentType, initialize_agent
from langchain_openai import OpenAI
from langchain_community.agent_toolkits.load_tools import load_tools

llm = OpenAI(temperature=0.2)
tools = load_tools(["wikipedia", "llm-math"], llm=llm)

agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)
result = agent.invoke("How to become the perfect AI/ML Developer")
print(result["output"])


#  Using the langgraph****************************************************************************************************************************************
# from langchain.agents import AgentType, initialize_agent
# from langgraph import LangGraph
# from langchain_openai import OpenAI
# from langchain_community.agent_toolkits.load_tools import load_tools

# # Initialize the LLM
# llm = OpenAI(temperature=0.2)

# # Initialize LangGraph for enhanced interaction
# lang_graph = LangGraph(llm)

# # Load tools with LangGraph
# tools = load_tools(["wikipedia", "llm-math"], llm=lang_graph)

# # Initialize the agent with LangGraph
# agent = initialize_agent(tools, lang_graph, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

# # Run the query
# print(agent.invoke("When was Elon Musk born? What is his age right now in 2023?"))
