# Exercise Tracking Application

## Overview
The Exercise Tracking Application is a Python-based tool designed to log and track physical activities. It uses the Nutritionix API to recognize and quantify various exercises based on user input. The application also features functionality to log these activities, potentially using a service like Sheety, for personal fitness tracking.

## Files in the Project
- `main.py`: The primary script that interacts with the Nutritionix API to track exercises and logs data using another web service.

## How to Set Up
1. Ensure Python is installed on your system, along with the `requests` module.
2. Obtain API keys for Nutritionix and any other service you intend to use (like Sheety) for logging data.
3. Store these keys as environment variables (`APP_ID`, `API_KEY`, `TOKEN`, and `SHEETY_ENDPOINT`).
4. Download the `main.py` file.
5. Update the `GENDER`, `WEIGHT_KG`, `HEIGHT_CM`, and `AGE` variables in `main.py` to reflect your personal data.
6. Run `main.py` and input your exercises to track and log them.

## Using the Application
- Input your physical activity details.
- The application uses the Nutritionix API to recognize and analyze the exercise.
- Exercise data is logged for tracking, using a service like Sheety.
- Keep track of your fitness journey efficiently and effectively.

## Dependencies
- Python 3.x
- `requests` module
- Nutritionix API
- Sheety or a similar web service for data logging

## Credits
This application is ideal for fitness enthusiasts looking to automate their exercise logging and tracking.

