import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [messages, setMessages] = useState([]);

  async function fetchMessages() {
    try {
      const response = await fetch('http://localhost:8000/messageList');
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }
      const data = await response.json();
      setMessages(data);
      console.log('Updated Messages List from backend: ',messages);
    } catch (error) {
      console.error('Error fetching messages:', error);
    }
  };

  useEffect(() => {
    fetchMessages();
  }, []);

  async function addMessages(message:any) {
    try{
      const response = await fetch("http://localhost:8000/addMessage", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "accept": "application/json"
        },
        body: JSON.stringify({senderName: 'User', text:message}),
      });
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }
      const data = await response.json(); //TODO: handle failure case better.
      console.log('Response Data from backend after addMessage POST Request: ', data);
      setMessages(data.messageList);
  } catch (error) {
    console.error('Error adding message:', error);  
  }
  }
  
  return (
    <div className="App">
      <header className="App-header">
        <Title/>
        <MessageList messages = {messages}/>
        <SendMessageForm addMessages = {addMessages}/>
      </header>
    </div>
  );
}

function MessageList({messages} : {messages:any}) {
  return(
    <ul className="message-list">                 
        {messages.map((message: any, index: any) => {
          return (
           <li className="messageListItem" key={index}>
             <div className="messageSenderInfoDiv">
               Sender: {message.senderName}
             </div>
             <div className="messageInfoDiv">
               Message: {message.text}
             </div>
           </li>
         )
       })}
     </ul>
  );
}

function Title() {
  return(
    <div>Chat UI</div>
  );
}

function SendMessageForm( {addMessages} : {addMessages:any}) {

  const [message, setMessage] = useState("")

  function handleSubmit(formData:any) {
    console.log("Data submitted by form: ",formData.get("textInput"))
    addMessages(formData.get("textInput"))
    setMessage("")
  }

  return(
    <form
        action={handleSubmit}
        className="send-message-form">
        <input
          name="textInput"
          placeholder="Type your message"
          />
        <button type="submit">Send</button>
      </form>
  );
}


export default App;
