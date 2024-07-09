from langchain_core.tools import Tool
from main.frontEndComponents.ux_agent.tools_funcs import create_html_files_wrapper, create_folder

TOOLS = [
    Tool(
        name='Site Map creator',
        func=create_html_files_wrapper,
        description="""This is a tool that takes the html code (str) and a filename (str) from the agent then parse 
        them and then call the create_html_files function to create a new html file at a specific location. the 
        function accepts a LIST composed of the HTML content and a filename"""
    ),
    Tool(
        name="Folder Creator",
        func=create_folder,
        description="""This is a tool that a foldername and then create a new folder with the foldername in a 
        specific location."""
    )
]