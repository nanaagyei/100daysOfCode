# ISS Overhead Notifier

## Overview
The ISS Overhead Notifier is a Python application that alerts users via email when the International Space Station (ISS) is close to their geographic location. It uses real-time ISS location data from an API and determines if the ISS is near the user's specified latitude and longitude. The application is ideal for space enthusiasts who want to know when to look up to spot the ISS.

## Files in the Project
- `main.py`: The main script that checks the ISS's location and sends email notifications.

## How to Set Up
1. Ensure Python is installed on your system, along with the `requests` and `smtplib` modules.
2. Download the `main.py` file.
3. Set your latitude and longitude in the `MY_LAT` and `MY_LONG` variables in `main.py`.
4. Update the `MY_EMAIL` variable and use an environment variable for `MY_PASSWORD` to store your email credentials securely.
5. Run `main.py`.

## Using the Application
- The script periodically checks the ISS's current location.
- If the ISS is overhead (close to your specified latitude and longitude), you'll receive an email notification.
- Ensure your email provider allows SMTP access for sending emails.

## Dependencies
- Python 3.x
- `requests` module for API calls
- `smtplib` module for email functionality
- `datetime` module
- `os` module for environment variables

## Credits
This application provides a unique way to connect with the wonders of space exploration.

