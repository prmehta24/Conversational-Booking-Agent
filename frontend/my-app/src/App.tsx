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
    },
  ]);

  function addMessages(message:any) {
    setMessageCount(messageCount + 1)
    setMessages([...messages, {messageId: messageCount, senderId: 'User', text:message}])
    console.log(messages)
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
        {messages.map((message: any) => {
          return (
           <li key={message.messageId}>
             <div>
               {message.senderId}
             </div>
             <div>
               {message.text}
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

  function handleSubmit() {
    addMessages(message)
    setMessage("")
  }

  function handleChange(e:any) {
    setMessage(e.target.value)
  }

  return(
    <form
        onSubmit={handleSubmit}
        className="send-message-form">
        <input
          onChange={handleChange}
          value={message}
          placeholder="Type your message and hit ENTER"
          type="text" />
      </form>
  );
}


export default App;
