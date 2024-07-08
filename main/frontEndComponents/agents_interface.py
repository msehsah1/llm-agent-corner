from abc import ABC, abstractmethod
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor


class Agent(ABC):
    def __init__(self, prompt, tools):
        self.prompt = prompt
        self.tools = tools

    def agent_init(self):
        """
        This method is for initializing the agent with a specific prompt and a specific set of tools depending on the
        functionality of the agent.
        :return: the agent executor
        """
        llm = ChatOpenAI(temperature=0.9, model="gpt-4-turbo")
        agent = create_react_agent(prompt=self.prompt, llm=llm, tools=self.tools)
        agent_executor = AgentExecutor(agent=agent, tools=self.tools, verbose=True)
        return agent_executor

    @abstractmethod
    @classmethod
    def agent_wrapper(cls):
        """
        This method is responsible for executing the agent.
        :return: the result of the invoke function
        """
        pass
