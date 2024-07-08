from main.frontEndComponents.agents_interface import Agent
from main.utils.utils import override
from main.frontEndComponents.prompt import REACT_AGENT_PROMPT, HTML_PROMPT_INSTRUCTION


class HTMLAgent(Agent):
    def __init__(self, prompt):
        super().__init__(prompt=prompt, tools="")

    @override
    @classmethod
    def agent_wrapper(cls, prompt):
        """
        This method is a wrapper method to invoke the frontend agent which need a prompt to instruct it to
        generate a html code which can be saved in the working directory using the tools provided
        :param prompt: prompt for the front end agent (instruction on what it will generate)
        :return: The result of the invoke method
        """
        react_prompt = REACT_AGENT_PROMPT.partial(instruction=HTML_PROMPT_INSTRUCTION)
        html_inst = cls(react_prompt)
        html_agent_executor = html_inst.agent_init()
        return html_agent_executor.invoke(input=prompt)
