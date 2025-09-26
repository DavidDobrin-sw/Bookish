
# Bookish

Say goodbye to dusty shelves, ink-stained fingers, and the whispers of the past. This project brings the classic library system into the 21st century with a modern, token-authenticated API for managing books, users, and lending.


## Quick Start

### Create a venv directory
Must be Python 3.9 or above

bash `python -m venv .venv`
    

### Activate the venv

bash ` source .venv/Scripts/activate`

cmd.exe `.venv\Scripts\activate.bat`

powershell `.venv\Scripts\Activate.ps1`

Linux / MacOS `source .venv/bin/activate`



### Deactivating the venv
Remember to deactivate the venv when you are done by running the command`deactivate`



### Install Poetry
Install `poetry` following the [link](https://python-poetry.org/docs/)

Install the python dependencies with the command `poetry install`



### Install npm dependencies
Run `npm install` to install the dependencies from within the client directory



### Run Flask
Run flask using `flask run` to test if the server will run locally



### Test the server is running
Make a response to `http://127.0.0.1:5000/healthcheck` to ensure the backend server is working either in the browser or by using [Postman](https://www.postman.com/)/[Thunder Client](https://www.thunderclient.com/)