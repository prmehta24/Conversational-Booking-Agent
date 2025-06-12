from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys

origins = [
    "http://localhost:3000",
]

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    senderName: str
    text: str
    

messageList = [Message(senderName="OpenAI", text="Hello, this is the first message.")]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/messageList")
def read_message_list():
    return messageList

@app.post("/addMessage")
def add_message(message: Message):
    messageList.append(message)
    return {"message": "Message added successfully", "messageList": messageList}

