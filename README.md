# Conversational-Booking-Agent
 a three-party booking system involving a Human user, an AI Assistant, and a Browser Agent. 

## Progress
* 30 min complete:
    * Updated Node/npm.
    * Setup project environment.
    * Decided on project architecture:
        * ReactJS + TS for Frontend Chat UI
        * Python for the backend. 
        * Use FastAPI to connect to an OpenAI backend for the AI assistant.
        * Use Playwright for browser automation.  
* 1 hour complete:
    * Updated App.tsx to start building the Chat UI. Updated README with link to the guide I am following to build a simple Chat UI.
* 1.5 hours complete:
    * Updated App.tsx with a component to display a list of messages and a form to enter a message. Debugging why the message list is not being entered when the form message is submitted.
* 2 hours complete:
    * Fixed bug in App.tsx - Now message list is being updated when form message is submitted. Adding css to make chat ui look better.
* 2.5 hours complete:
    * Set up python virtual environment. Installed FastAPI. 
    * Created a file for the Python backend code.
* 3 hours complete:
    * Updated frontend code to use index in message list as key for li elements.
    * Added API endpoints in python backend to return messagelist and add new messages to messagelist stored in backend.
* 3.5 hours complete:
    * Got backend server to run with API endpoints and tested them out with Swagger.
    * Debugged encoding error with starting backend server and compilation errors with main.py.
    * Added some instructions to run both servers to the README.
* 4 hours complete:
    * Rewired frontend to fetch messagesList to display from backend.
    * Updating backend to fix 'blocked by CORS policy' issue.

# Instructions to Run
* To active virtual env with git bash: 'source .venv/Scripts/activate'
* To run frontend:
    * "cd my-app"
    * "npm start"
* To run backend:
    * "fastapi run main.py"

## References
* https://medium.com/free-code-camp/how-to-build-a-react-js-chat-app-in-10-minutes-c9233794642b
* https://fastapi.tiangolo.com/

