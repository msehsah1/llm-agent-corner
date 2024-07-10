from langchain_core.tools import Tool
from main.frontEndComponents.ux_agent.tools_funcs import create_site_map

TOOLS = [
    Tool(
        name='Site Map creator',
        func=create_site_map,
        description="""This is a tool that takes unformatted reponse of a site map from the agent then parse 
        them and then call the create_site_map function to parse the result"""
    )
]