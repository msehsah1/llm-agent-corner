from main.frontEndComponents.agents_interface import Agent
from main.utils.utils import override
from main.frontEndComponents.prompt import REACT_AGENT_PROMPT, HTML_PROMPT_INSTRUCTION
from main.frontEndComponents.html_agent.tools import TOOLS


class HTMLAgent(Agent):
    def __init__(self, prompt, tools):
        super().__init__(prompt=prompt, tools=tools)

    @classmethod
    def agent_wrapper(cls, prompt):
        """
        This method is a wrapper method to invoke the frontend agent which need a prompt to instruct it to
        generate a html code which can be saved in the working directory using the tools provided
        :param prompt: prompt for the front end agent (instruction on what it will generate)
        :return: The result of the invoke method
        """
        print("I am in the wrapper method!")
        react_prompt = REACT_AGENT_PROMPT.partial(instructions=HTML_PROMPT_INSTRUCTION)
        tools = TOOLS
        html_inst = cls(react_prompt, tools)
        html_agent_executor = html_inst.agent_init()
        return html_agent_executor.invoke(input=prompt)

    @staticmethod
    def test(prompt):
        print("I am in the test method!")
        return HTMLAgent.agent_wrapper(prompt)
