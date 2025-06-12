from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

chat = client.chats.create(model="gemini-2.0-flash", 
    config=types.GenerateContentConfig(
        system_instruction="The AI Assistant should engage the Human user in a dialogue" \
        " to collect all necessary booking details (name, email, date, time" \
        "). The assistant should ask for any " \
        "missing information and confirm details with the user."))
response = chat.send_message("Hello there!")
print(response.text)