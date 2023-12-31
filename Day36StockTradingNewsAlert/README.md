# Stock Price Alert Application

## Overview
The Stock Price Alert Application is a Python tool designed to monitor the stock price of Tesla Inc. It fetches stock data and relevant news articles, sending updates via SMS. The application utilizes financial data from Alpha Vantage and news from NewsAPI, with Twilio for SMS messaging.

## Files in the Project
- `main.py`: The main script of the application, which includes logic for fetching stock data, news, and sending SMS alerts.

## How to Set Up
1. Ensure Python is installed on your system, along with the `requests` and `twilio` modules.
2. Obtain API keys from Alpha Vantage, NewsAPI, and Twilio, and store them as environment variables.
3. Download the `main.py` file.
4. Set environment variables for `NEWS_API_KEY`, `STOCK_API_KEY`, and Twilio credentials.
5. Run `main.py` to start monitoring stock prices and receive alerts.

## Using the Application
- The application monitors Tesla's stock price.
- If significant changes are detected, it fetches relevant news articles.
- Alerts, including stock price changes and news, are sent via SMS.
- Customize the script for different companies or additional functionalities.

## Dependencies
- Python 3.x
- `requests` module for API calls
- `twilio` module for SMS messaging

## Credits
This application is useful for investors and enthusiasts interested in staying updated with market movements and relevant news.

