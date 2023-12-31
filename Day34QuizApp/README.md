# Quiz Application

## Overview
This Quiz Application is a Python-based interactive quiz game. It utilizes an API to fetch quiz questions and presents them to the user in a graphical interface. The application is designed to test knowledge in a fun and engaging way, keeping track of scores and providing a variety of questions.

## Files in the Project
- `main.py`: The main script that initializes the quiz game.
- `data.py`: Handles fetching quiz questions from an online API.
- `question_model.py`: Defines the `Question` class for structuring quiz questions.
- `quiz_brain.py`: Contains the `QuizBrain` class, managing the quiz logic and scoring.
- `ui.py`: Implements the `QuizUI` class, creating a graphical user interface using `tkinter`.

## How to Set Up
1. Ensure Python is installed on your system, along with the `requests` and `tkinter` modules.
2. Download all the project files (`main.py`, `data.py`, `question_model.py`, `quiz_brain.py`, `ui.py`).
3. Run `main.py` to start the quiz.

## Using the Application
- The application fetches a set of questions and presents them one by one.
- Answer each question in the GUI, and the application will track your score.
- At the end of the quiz, your total score is displayed.
- Enjoy a variety of questions each time you play.

## Dependencies
- Python 3.x
- `requests` module for fetching data from the API
- `tkinter` module for the GUI

## Credits
This quiz application is perfect for anyone looking to test their knowledge in a wide range of subjects in a fun and interactive way.
