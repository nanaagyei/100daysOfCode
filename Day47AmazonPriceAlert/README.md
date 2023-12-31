# Amazon Price Tracker

## Overview
The Amazon Price Tracker is a Python application designed to monitor the price of a product on Amazon and send email notifications when the price changes. It employs web scraping techniques using `requests` and `BeautifulSoup` to extract product price information and `smtplib` to send email alerts. This tool is useful for keeping track of price changes on desired products.

## Files in the Project
- `main.py`: The primary script that scrapes Amazon product pages, checks for price changes, and sends email notifications.

## How to Set Up
1. Ensure Python is installed on your system, along with the `requests`, `bs4` (BeautifulSoup), `lxml`, and `smtplib` modules.
2. Set your Amazon product page URL in the `AMAZON_URL` variable in `main.py`.
3. Update the `MY_EMAIL` variable and use an environment variable for `MY_PASSWORD` to store your email credentials securely.
4. Specify the `RECIPIENT_ADDRESS` for where to send the notifications.
5. Download the `main.py` file.
6. Run `main.py` to start monitoring the specified Amazon product.

## Using the Application
- The script checks the price of a product on its Amazon page.
- If a price change is detected, it sends an email alert to the specified recipient.
- Customize the script for different products or to modify the notification criteria.

## Dependencies
- Python 3.x
- `requests` and `bs4` (BeautifulSoup) for web scraping
- `lxml` for parsing HTML
- `smtplib` for sending emails

## Credits
Developed by Prince Agyei Tuffour. This application is ideal for anyone who wants to stay updated on price changes for their favorite products on Amazon.

