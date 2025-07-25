# Conversational-Booking-Agent

To book a meeting on Calendly by chatting with an AI assistant powered by Gemini. Chat UI built with React.js and TypeScript. 

## Instructions to Run
* Prerequisites
    * [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
    * [Node](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
    * [Python](https://www.python.org/downloads/)
    * [Gemini API Key](https://ai.google.dev/gemini-api/docs/quickstart)
* Install frontend dependencies.
    * Go to frontend/my-app
    * Run `npm install`
* Install backend dependencies.
    * Go to the backend folder.
    * Create a [Python venv](https://docs.python.org/3/library/venv.html).
    * [Activate the venv](https://docs.python.org/3/library/venv.html#how-venvs-work).
    * `pip install -r requirements.txt`
* Create a .env file in the backend folder and save two lines:
    * GEMINI_API_KEY=api_key_value_here
    * CALENDLY_BOOKING_URL=https://calendly.com/your_booking_url
* To run backend:
    * Go to backend folder. 
    * [Activate the venv](https://docs.python.org/3/library/venv.html#how-venvs-work). To activate virtual env with git bash: `source .venv/Scripts/activate` (replace .venv by the name of the virtual environment folder you created  ) 
    * Set `PYTHONIOENCODING=utf-8` environment variable in case of UnicodeEncodeError when starting backend server. Refer reference link 3.
    * `fastapi run main.py`
* To run frontend:
    * `cd frontend/my-app`
    * `npm start`
* Once both backend and frontend are running, 
    * you can access the Chat UI at `http://localhost:3000/`. 
    * The backend docs are available at `http://localhost:8000/docs`

## Notes
* The browser automation can fail several times with the same inputs before succeeding. If the response from the booking agent is 'Please try again', it is a booking automation failure, not invalid inputs given to the agent. So, request the agent to try again multiple times until it succeeds.
* More information regarding this project can be found in the ProjectReport.pdf
* A video walkthrough of the project can be found [here](https://www.loom.com/share/6875153af4bd429bb5f920181e0409f8?sid=3752eb88-4d9f-44d0-8426-c4f3cdde87ef).
* The frontend is made roughly to complete the project within the time constraints.

## Progress
* 30 min complete:
    * Updated Node/npm.
    * Setup project environment.
    * Decided on project architecture:
        * ReactJS + TS for Frontend Chat UI
        * Python for the backend. 
        * Use FastAPI to connect to a Google Gemini backend for the AI assistant.
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
* 4.5 hours complete:
    * Fixed CORS issue with backend.
    * Cleaned up logs in frontend.
    * Updated addMessage function in frontend to send a POST request to the backend addMessage endpoint.
* 5 hours complete:
    * Found out that OpenAI API was paid. Surveyed free OpenAI API alternatives and decided on the Gemini API.
    * Got the API key, made a .env file, and tested out the API.
* 5.5 hours complete:
    * Updated model.py to use Gemini API Chat SDK. This retains chat history for the AI assistant to use as context.
* 6 hours complete:
    * Added a function to send a message to the AI and get a response. Integrated this function into the addMessage function.
    * Used the above mentioned function to initialise the messageList with an AI message.
    * Added function declaration for calendly booking function. Gave info about booking function to AI.
* 6.5 hours complete:
    * Built out calendly booking function.
    * Updated get ai response function to identify when the ai response is requesting a function call.
* 7 hours complete:
    * Debugging calendly booking function.
* 7.5 hours complete:
    * Updated calendly booking function to locate Next button element to click properly.
* 8 hours complete:
    * Updated book meeting function declaration to include expected time and date formats
    * Updated model get_ai_response function to call book_meeting function
    * Added error handling to book_meeting function. Got book_meeting to work consistently and return a response. Debugged playwright code to make it work with fastapi server.
* 8.5 hours complete:
    * Updated booking logic to mention this is a test booking in the additional info section when booking.
    * Added better error handling and more useful error responses to the booking logic.
* 9 hours complete:
    * Modified code to work for any calendly booking url.
    * Cleaned up unnecessary imports, added comments, and debugged error related to selecting wrong time during booking using playwright. I was using an ambiguous element selector.
    * Reread the assignment document to figure out what is left to do.
* 9.5 hours complete:
    * Created list of tasks left to do and began writing the project report.
* 10 hours complete:
    * Continued writing the project report - Explained architecture, why I chose the tech stack, separation of logic in the codebase, future work, etc.
* 10.5 hours complete:
    * Added comments to code.
    * Improved instructions to run project in README.
    * Updated Project Report - Added my approach on how I would handle bonus objectives, added more future planned work(UI updates, potential failure flows to handle, changes to make backend code more clear/faster/reliable), etc.
* 11 hours complete:
    * Updated Project Report - Added my approach on how I would handle bonus objectives, adding what I accomplished and learned from the assessment, future work, etc.
* 11.5 hours complete:
    * Updated Project Report - Added what I accomplished and learned from the assessment, future work, justification for use of Playwright, etc.
* 12.5 hours complete:
    * Updated README to have complete instructions on how to setup and run the project.
    * Completed the Project Report.
    * Added a requirements.txt to install python dependencies.
* 13 hours complete:
    * Updated Project Report and created a pdf.
    * Added informative comments and TODO comments to the project.
* 15 hours complete:
    * Updated Project Report with more planned future work.
    * Created a Loom video walking through the project objective, architecture, README, write-up, and did a project demo.

## Tools Used
* Github Copilot
* Visual Studio Code

## References
1. https://medium.com/free-code-camp/how-to-build-a-react-js-chat-app-in-10-minutes-c9233794642b
2. https://fastapi.tiangolo.com/
3. https://stackoverflow.com/questions/79199890/fastapi-dev-fails-with-unicodeencodeerror
4. https://fastapi.tiangolo.com/tutorial/cors/#use-corsmiddleware
5. https://stackoverflow.com/questions/72253011/is-it-possible-to-initialize-the-state-of-a-component-with-api-data-before-the-i
6. https://ai.google.dev/gemini-api/docs/quickstart
7. https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1
8. https://stackoverflow.com/questions/2349991/how-do-i-import-other-python-files
9. https://ai.google.dev/gemini-api/docs/function-calling?example=meeting
10. https://playwright.dev/python/docs/api/class-selectors#selectors-set-test-id-attribute
11. https://stackoverflow.com/questions/75151754/how-can-i-select-an-element-by-id
12. https://stackoverflow.com/questions/79109458/playwright-python-how-can-i-catch-exception-and-just-gracefully-quit
13. https://www.markdownguide.org/basic-syntax/
