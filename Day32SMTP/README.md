# Automatic Birthday Email Sender

## Overview
The Automatic Birthday Email Sender is a Python application designed to automatically send birthday emails. It checks a list of birthdays and, if there's a match with the current date, sends a personalized birthday email. The application uses `datetime` to manage dates, `pandas` for reading birthday data, and `smtplib` for email sending.

## Files in the Project
- `main.py`: The main script that handles birthday checks and email sending.
- `birthdays.csv`: A CSV file containing the list of birthdays (ensure this file is present in the project directory).
- `letter_templates`: A directory containing various birthday letter templates.

## How to Set Up
1. Ensure Python is installed on your system, along with the required modules (`pandas`, `smtplib`).
2. Download the `main.py` file, `birthdays.csv`, and the `letter_templates` directory.
3. Update the `MY_EMAIL` and `MY_PASSWORD` variables in `main.py` with your email credentials.
4. Run `main.py` to start the application.

## Using the Application
- The application checks the current date against the `birthdays.csv` file.
- If a birthday matches today's date, it selects a random letter template and personalizes it.
- The script then sends an email to the birthday person.
- Ensure your email provider allows SMTP access and that you handle email credentials securely.

## Dependencies
- Python 3.x
- `datetime` module
- `pandas` module
- `random` module
- `smtplib` module

## Credits
This application is perfect for ensuring you never forget to send a birthday wish again.

