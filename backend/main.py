from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import get_ai_response
import sys

origins = [
    "http://localhost:3000",
]

sys.stdin.reconfigure(encoding='utf-8') #TODO: Check if this is needed.
sys.stdout.reconfigure(encoding='utf-8')

app = FastAPI()

app.add_middleware( #TODO: understand how the various parameters work.
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    senderName: str
    text: str
    

messageList = []
# initialise the messageList.
ai_response = get_ai_response("Hi!")
if ai_response:
    ai_message = Message(senderName="AI", text=ai_response)
    messageList.append(ai_message)
else:
    ai_message = Message(senderName="AI", text="Sorry, I am having trouble connecting to the AI service.")
    messageList.append(ai_message)

@app.get("/")
def read_root():
    return {"Hello": "World"} #TODO: Change this to a more meaningful message.

@app.get("/messageList")
def read_message_list():
    return messageList

@app.post("/addMessage")
def add_message(message: Message): #TODO: Am I handling all possible errors here?
    messageList.append(message)
    ai_response = get_ai_response(message.text)
    if ai_response:
        ai_message = Message(senderName="AI", text=ai_response)
        messageList.append(ai_message)
    else:
        ai_message = Message(senderName="AI", text="Sorry, I couldn't process your request.")
        messageList.append(ai_message)
    return {"message": "Message added successfully", "messageList": messageList}

