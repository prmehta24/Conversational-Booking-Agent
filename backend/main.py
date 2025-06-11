from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Message(BaseModel):
    senderName: str
    text: str

    def __init__(self, senderName: str, text: str):
        self.senderName = senderName
        self.text = text
    

messageList = [Message("OpenAI", "Hello, this is the first message.")]

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

