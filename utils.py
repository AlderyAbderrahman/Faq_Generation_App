import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure with environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_faq(text):
    prompt = f"""From the following text, generate a list of 5–10 Frequently Asked Questions with answers.
Be concise, helpful, and use simple language.

Text: {text}
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating FAQ: {str(e)}"