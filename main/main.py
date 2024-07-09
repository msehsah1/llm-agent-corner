import os
from dotenv import load_dotenv
from pathlib import Path
import logging
from main.frontEndComponents.agents_interface import Agent
from main.frontEndComponents.html_agent.html_agent import HTMLAgent
from main.frontEndComponents.prompt import HTML_PROMPT_INPUT

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """
    Main function to run the application.
    This is the entry point.
    """
    load_environment()
    print("Hello and welcome to the application!")
    HTMLAgent.test(HTML_PROMPT_INPUT)


def load_environment():
    """
    Load environment variables from the .env file.
    """
    env_path = Path('config') / '.env'
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
        logger.info("Environment variables loaded from .env file.")
    else:
        logger.warning(".env file not found. Make sure to create one if environment variables are needed.")


if __name__ == '__main__':
    main()
