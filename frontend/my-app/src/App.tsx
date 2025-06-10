import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [messages, setMessages] = useState([
    {
      senderId:'OpenAI',
      text: "Hi, I'm ChatGPT"
    },
  ]);
  return (
    <div className="App">
      <header className="App-header">
        <Title/>
        <MessageList messages = {messages}/>
        <SendMessageForm/>
      </header>
    </div>
  );
}

function MessageList({messages} : {messages:any}) {
  return(
    <ul className="message-list">                 
        {messages.map((message: any) => {
          return (
           <li key={message.id}>
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
    <div>Title</div>
  );
}

function SendMessageForm() {
  return(
    <div>SendMessageForm</div>
  );
}


export default App;
