from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from booking import book_meeting

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
                "description": "Date of the meeting (e.g., '2025-07-10')",
            },
            "time": {
                "type": "string",
                "description": "Time of the meeting (e.g., '10:30am', '3:00pm')",
            },
        },
        "required": ["name", "email", "date", "time"],
    },
}

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)
tools = types.Tool(function_declarations=[schedule_meeting_function])

chat = client.chats.create(model="gemini-2.0-flash",  #TODO: Experiment with other models.
    config=types.GenerateContentConfig(
        tools=[tools],
        system_instruction="The AI Assistant should engage the Human user in a dialogue" \
        " to collect all necessary booking details (name, email, date, time" \
        "). The assistant should ask for any " \
        "missing information and confirm details with the user."))

def get_ai_response(user_message):
    response = chat.send_message(user_message)
    print(f"AI Response: {response}")
    if response.candidates[0].content.parts[0].function_call:
        function_call = response.candidates[0].content.parts[0].function_call
        print(f"Function to call: {function_call.name}")
        print(f"Arguments: {function_call.args}")
        result = book_meeting(**function_call.args) 
        return result #TODO: Send the result value back to the AI and return the AI's response.
    else:
        print(f"AI Response Message: {response.text}")
        return response.text