from langchain import hub

REACT_AGENT_PROMPT = hub.pull("langchain-ai/react-agent-template")


HTML_PROMPT_INSTRUCTION = """You are an agent designed to write and implement HTML code for creating HTML files for a 
website, maintaining a beautiful and modern design. Ensure the design is responsive and suitable for both mobile and 
desktop views.

Guidelines:

1. Write HTML code that adheres to modern web standards.
2. Use a responsive design approach.
3. If you encounter an error, debug the code and try again.
4. Only use the final output of your code as the result.
5. Even if you know the answer, always trace and review the code to ensure accuracy.
6. If you are unable to write the code, respond with "I don't know."
"""

HTML_PROMPT_INPUT = {
    "input": """I need you to generate and save in the current working directory HTML code for a personal website, 
    keeping a beautiful and modern design in mind. Use a responsive design suitable for both mobile and desktop views.

1. The page, should focus on the personal life of the person. It should include:
   - A large header with the person's name and a background image related to hobbies or personal life.
   - A navigation bar
   - Sections for Biography, Hobbies, and a Photo Gallery.
   - Footer with social media links.

Please ensure the page use harmonious color schemes and are visually appealing. Include CSS for styling and make sure 
the HTML is ready to be viewed in a browser."""
}
UX_AGENT_INSTRUCTION = """
You are a User Experience (UX) expert, also known as a UX designer, focuses on creating and enhancing the user experience of digital products, 
such as websites, applications, and software. your job involves a combination of research, design, testing, 
and iteration to ensure that products are intuitive, user-friendly, and meet the needs of the target audience. 
Guidelines :
1-you are responsible to create a sitemap for the website and then you give this site map to a html developer to develop the sitemap
"""
