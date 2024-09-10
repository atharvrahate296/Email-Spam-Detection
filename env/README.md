# **Rock Paper Scissors Game**

This is a simple web-based Rock Paper Scissors game developed using Flask. The game allows a user to play against the computer, which randomly selects its move.

## Prerequisites

**Python 3.x:** Ensure you have Python installed on your system. You can download it from the official Python website.
**Flask:** A lightweight WSGI web application framework in Python. Flask makes it easy to get started with web development. Install it using pip install flask.

## General Rules for Usage

**Start the Application:**
- Navigate to the project directory.
- Run the Flask application :
                on terminal type : -> python main.py
- Open your web browser and go to http://127.0.0.1:5000.

**Playing the Game:**

- On the homepage, select your choice (Rock, Paper, or Scissors) by clicking on the corresponding button.
- Click the "Submit" button to submit your choice.
- The result page will display whether you won, lost, or tied the round, along with the appropriate background color indicating the results:
    - **Green:** You won the round.
    - **Red:** The computer won the round.
    - **Blue:** The round was a tie.
- To play again, click the "Replay" button on the result page.

## Game Logic

The game consists of the following logic:

- The user selects their choice (Rock, Paper, or Scissors) via a form.
- The computer randomly selects its choice.
- The winner is determined based on traditional Rock Paper Scissors rules:
  - Rock beats Scissors
  - Scissors beat Paper
  - Paper beats Rock
  - If both choices are the same, it is a tie.

## Flask Routes

- **`/`** (GET and POST): 
  - **GET**: Renders the homepage where the user can select their choice.
  - **POST**: Processes the user's choice, computes the result, and renders the result page with the outcome.

## Application Structure

- `main.py`: Main application file containing the Flask routes and game logic.
- `templates/`: Directory containing HTML templates for the homepage and result page.
- `static/`: Directory containing static files for execution(images,css stylesheets,etc).

## HTML Templates

- `home.html`: The homepage where the user can choose Rock, Paper, or Scissors.
- `result.html`: The result page that displays whether the user won, lost, or tied the round, along with appropriate styling based on the outcome.


## Conclusion

This simple Rock Paper Scissors game demonstrates the basics of using Flask to handle user input, process game logic, and render HTML templates based on the game's outcome. Enjoy playing and tweaking the game to add more features or improve the design!