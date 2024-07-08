from main.frontEndComponents.agents_interface import Agent
from main.utils.utils import override


class HTMLAgent(Agent):
    def __init__(self):
        super().__init__(prompt="", tools="")

    @override
    @classmethod
    def agent_wrapper(cls, prompt):
        """
        This method is a wrapper method to invoke the frontend agent which need a prompt to instruct it to
        generate a html code which can be saved in the working directory using the tools provided
        :param prompt: prompt for the front end agent (instruction on what it will generate)
        :return: The result of the invoke method
        """
        html_inst = cls()
        html_agent_executor = html_inst.agent_init()
        return html_agent_executor.invoke(input=prompt)
