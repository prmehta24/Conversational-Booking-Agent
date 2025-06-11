import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [messageCount, setMessageCount] = useState(1);
  const [messages, setMessages] = useState([
    {
      messageId: 1,
      senderId:'OpenAI',
      text: "Hi, I'm ChatGPT"
    }
  ]);

  function addMessages(message:any) {
    setMessageCount(messageCount + 1)
    setMessages([...messages, {messageId: (messageCount+1), senderId: 'User', text:message}])
    console.log(messages)
  }
  console.log(messages)
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
        {messages.map((message: any) => {
          return (
           <li className="messageListItem" key={message.messageId}>
             <div className="messageSenderInfoDiv">
               Sender: {message.senderId}
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
    console.log(formData.get("textInput"))
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
