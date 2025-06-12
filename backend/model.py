from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# Define the function declaration for the model
schedule_meeting_function = {
    "name": "schedule_meeting",
    "description": "Schedules a meeting at a given time and date.",
    "parameters": {
        "type": "object",
        "properties": {
        "name": {
                "type": "string",
                "description": "Name of the person scheduling the meeting.",
            },
            "email": {
                "type": "string",
                "description": "Email address of the person scheduling the meeting.",
            },
            "date": {
                "type": "string",
                "description": "Date of the meeting (e.g., '2024-07-29')",
            },
            "time": {
                "type": "string",
                "description": "Time of the meeting (e.g., '15:00')",
            },
        },
        "required": ["attendees", "date", "time", "topic"],
    },
}

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)
tools = types.Tool(function_declarations=[schedule_meeting_function])

chat = client.chats.create(model="gemini-2.0-flash", 
    config=types.GenerateContentConfig(
        system_instruction="The AI Assistant should engage the Human user in a dialogue" \
        " to collect all necessary booking details (name, email, date, time" \
        "). The assistant should ask for any " \
        "missing information and confirm details with the user."))

def get_ai_response(user_message):
    response = chat.send_message(user_message)
    print(f"AI Response: {response.text}")
    return response