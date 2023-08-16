import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "7DYB6KTLIQ6BU0UH"
NEWS_API_KEY = "c228162cf79c4a93beaccc3795420b2c"
TWILIO_SID = "AC6297a1e76f4b220eb88560885ca1baf8"
AUTH_TOKEN = os.environ.get("API_KEY")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

NEWS_PARAMS = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
}


response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

diff_percent = (difference / float(yesterday_closing_price)) * 100
if diff_percent > 1:
    news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMS)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)

    client = Client(TWILIO_SID, AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            from_='+13083373817',
            body=article,
            to='+36302304217'
        )


