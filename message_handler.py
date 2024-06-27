import os

import google.generativeai as genai
from dotenv import load_dotenv

def get_google_api_key():
    """
    Retrieve the OpenAI API key from the environment variable.

    Returns:
        str: The OpenAI API key.
    """
    load_dotenv()
    return os.environ.get("GOOGLE_API_KEY")


def gemini_response(query):
    genai.configure(api_key=get_google_api_key())
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(query)
    return response.text
