import ast
import os


def create_html_files(html_code: str, filename: str = "default_filename.html"):
    """
    This function creates HTML files from the given html code and saves them with the provided filename.
    :param html_code: str representing the html code
    :param filename: str representing the filename
    :return: str representing the status of the file
    """
    filename = "resources/" + filename
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html_code)
    return f"HTML file created: {filename}"


def create_html_files_wrapper(args):
    """
    Wrapper function to handle tool calls with multiple arguments
    which will call the create_html_files function to save the html code into a file.
    :param args: str representing the arguments in the form of a list
    :return: list with the html code and the filename
    """
    args = args.literal_eval(args)
    html_code = args[0]
    filename = args[1]
    return create_html_files(html_code, filename)


def create_folder(foldername: str):
    """
    Create a new folder with a the specific foldername if it does not exist.
    """
    path = "resources/" + foldername
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Folder created at {path}")
        else:
            print("Folder already exists.")
        return f"folder {foldername} has been created"
    except Exception as e:
        print(f"An error occurred: {e}")
