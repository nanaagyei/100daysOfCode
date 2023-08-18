import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = "d6ece9ed1c7746cbbf53674de66c5479"
STOCK_API_KEY = "E3Q54Z9NH7ARYFIU"


def get_news():
    news_parameters = {
        "q": STOCK_NAME.lower(),
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY,
    }

    news_api_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_api_response.raise_for_status()
    news_data = news_api_response.json()

    articles = news_data["articles"][:3]

    # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    headlines_descriptions = [[article["title"], article["description"], article["url"]] for article in articles]

    account_sid = "ACf1e6d54e563a0541b841bf3ae121d7d4"
    auth_token = "c1a86dbbbf568c12e36796ab9fc40705"

    for article in headlines_descriptions:
        headline = article[0]
        brief = article[1]
        url = article[2]
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=f"{STOCK_NAME}: {ticker}\n"
                     f"Headline: {headline}.\n"
                     f"Brief: {brief}.\n"
                     f"News: {url}",
                from_='+18669846216',
                to='+16232733354'
            )

        return message.status


stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
time_series_stock = stock_data["Time Series (Daily)"]

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

closing_prices = [float(prices["4. close"]) for (date,prices) in time_series_stock.items()]
yesterday_closing_price = closing_prices[0]


day_before_yesterday = closing_prices[1]

price_diff = abs(yesterday_closing_price - day_before_yesterday)


percent_diff = (price_diff/day_before_yesterday) * 100

ticker = ""
if yesterday_closing_price - day_before_yesterday < 0:
    ticker = f"🔻{percent_diff}%"
else:
    ticker = f"🔺{percent_diff}%"

if percent_diff > 1:
    print(get_news())
else:
    print("No major change")
    # STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds 
and prominent investors are required to file by the SEC The 13F filings show 
the funds' and investors' portfolio positions as of March 31st, near the height 
of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and 
prominent investors are required to file by the SEC The 13F filings show the 
funds' and investors' portfolio positions as of March 31st, near the height of 
bthe coronavirus market crash.
"""

