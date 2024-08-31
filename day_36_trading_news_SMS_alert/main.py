import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import json
from twilio.rest import Client
from time import sleep

load_dotenv("../.env")
STOCK = "TSLA"
NEWS_QUERY = '"Tesla Inc" OR "Tesla Motors" OR "Elon Musk" OR "TSLA"'


def save_data(filename: str, data_name):
    with open(f"data/{filename}.json", 'w') as data:
        print(f"creating the file...{filename}\n")
        json.dump(data_name, data, indent=4)


def getting_data(filename):
    with open(f"data/{filename}.json", 'r') as data:
        print(f"reading the file....{filename}\n")
        return json.load(data)


class SMSTradingNews:
    def __init__(self):

        # getting the yesterday and the day before date
        self.yesterday = datetime.now() - timedelta(days=1)
        self.day_before_yesterday = datetime.now() - timedelta(days=2)

        # fetching the data if we don't have any data(for testing)
        try:
            self.price_data = getting_data("price_data")
        except FileNotFoundError:
            self.price_data = self.price_req().json()["Time Series (Daily)"]
            save_data("price_data", self.price_data)

        try:
            self.news_data = getting_data("news_data")
        except FileNotFoundError:
            self.news_data = self.news_req().json()["articles"]
            save_data("news_data", self.news_data)

        # getting the percentage difference between the closing price from tomorrow and the day before
        self.percentage_diff = self.calc_percentage_diff()

        # setting up the client for text message API
        self.account_sid = os.getenv("PHONE_NUMBER_SID")
        self.auth_token = os.getenv("AUTH_PHONE_TOKEN")
        self.client = Client(self.account_sid, self.auth_token)

        self.main_logic()

    def price_req(self):
        stock_endpoint = "https://www.alphavantage.co/query"
        stock_price_parameters = {
            "function": "TIME_SERIES_DAILY",
            "outputsize": "compact",
            "symbol": STOCK,
            "apikey": os.getenv("ALPHAVANTAGE_API_KEY")
        }
        response = requests.get(url=stock_endpoint, params=stock_price_parameters)
        response.raise_for_status()
        return response

    def news_req(self):
        news_endpoint = "https://newsapi.org/v2/everything?"
        stock_news = {
            "qInTitle": NEWS_QUERY,
            "from": self.day_before_yesterday.strftime("%Y-%m-%d") + "T01:00",
            "to": self.yesterday.strftime("%Y-%m-%d") + "T01:00",
            "sortBy": "relevancy",
            "language": "en",
            "pageSize": 10,
            "apiKey": os.getenv("NEWSAPI_KEY"),
        }
        stock_news = requests.get(url=news_endpoint, params=stock_news)
        stock_news.raise_for_status()
        return stock_news

    # calculation percentage difference between yesterday and day before
    def calc_percentage_diff(self):
        value1 = float(self.price_data[self.yesterday.strftime("%Y-%m-%d")]["4. close"])
        value2 = float(self.price_data[self.day_before_yesterday.strftime("%Y-%m-%d")]["4. close"])
        result = abs(value1 - value2) / ((value1 + value2) / 2) * 100
        return round(result, 2)

    def message_constructor(self, data_structure):
        if self.percentage_diff > 0:
            symbol = "🔺"
        else:
            self.percentage_diff *= -1
            symbol = "🔻"
        text_message = f"""
        {STOCK}: {symbol} {self.percentage_diff}%\nHeadline: {data_structure["title"]}\nBrief: {data_structure["description"]}
        """
        return text_message

    def main_logic(self):
        send_limit = 3
        for i in self.news_data:
            if send_limit != 0:
                text_message = self.message_constructor(i)
                message = self.client.messages.create(
                    body=f"\n{text_message}",
                    from_=os.getenv("VIRTUAL_PHONE"),
                    to=os.getenv("SEND_TO"),
                )
                print(text_message)
                send_limit -= 1
                sleep(5)
            else:
                break


if __name__ == '__main__':
    app = SMSTradingNews()
