# Flight Deal Finder Application

## Overview
The Flight Deal Finder Application is a comprehensive tool designed to track and find the best flight deals. It interacts with flight deal data sources and APIs to fetch current flight prices and details, manages the data using a spreadsheet or similar service, and sends notifications about the best deals.

## Files in the Project
- `main.py`: The main script that orchestrates the workflow of the application.
- `data_manager.py`: Manages interactions with the data source (e.g., Google Sheet) for flight deals.
- `flight_search.py`: Handles communication with a Flight Search API to retrieve flight information.
- `flight_data.py`: Structures the flight data for easy handling and access.
- `notification_manager.py`: Sends notifications, such as emails, with details about deal flights.

## How to Set Up
1. Ensure Python is installed on your system, along with the `requests` and `smtplib` modules.
2. Obtain necessary API keys for flight data and set up a data source (like a Google Sheet) for managing flight deals.
3. Store API keys and sensitive information as environment variables or securely within the scripts.
4. Download all the project files and place them in the same directory.
5. Run `main.py` to start the application.

## Using the Application
- The application regularly checks for flight deals using specified criteria (destinations, prices, dates).
- It updates the flight deal data source with the latest information.
- When a good deal is found, it sends a notification with the flight details.
- Customize the scripts to fit specific needs, such as different destinations, airlines, or notification methods.

## Dependencies
- Python 3.x
- `requests` module for API calls
- `smtplib` module for email notifications

## Credits
Developed by Prince Agyei Tuffour. This application is perfect for travelers looking for the best flight deals and wanting to automate the search and notification process.

