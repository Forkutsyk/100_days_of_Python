import os
import requests
from dotenv import load_dotenv
import json
from datetime import datetime as dt
from twilio.rest import Client

load_dotenv("../.env")


def get_data():
    parameters = {
        "lat": 52.808369,
        "lon": 9.96374,
        "appid": os.getenv("WEATHER_DATA_API_KEY"),
        "cnt": 7,
    }
    endpoint_url = f"https://api.openweathermap.org/data/2.5/forecast"
    print("Getting data...\n")
    response = requests.get(url=endpoint_url, params=parameters)
    response.raise_for_status()

    return response.json()


class RainAlertAPP:
    def __init__(self):
        try:
            with open("weather_data.json", 'r') as data:
                print("reading the file....\n")
                self.data = json.load(data)

        except FileNotFoundError:
            with open("weather_data.json", 'w') as data:
                print("creating the file...\n")
                self.data = get_data()
                json.dump(self.data, data, indent=4)

        # setting up message client
        self.account_sid = os.getenv("PHONE_NUMBER_SID")
        self.auth_token = os.getenv("AUTH_PHONE_TOKEN")
        self.client = Client(self.account_sid, self.auth_token)

        self.weather_for_21h = self.data['list']
        self.rain_alert()

    def check_data_relevance(self):
        data_date = int(self.weather_for_21h[0]["dt_txt"].split(" ")[0].split("-")[2])
        today = int(dt.now().day)
        if data_date != today:
            print("The data is not relevant. Parsing a new data...\n")
            self.data = get_data()
            self.weather_for_21h = self.data['list']
            with open("weather_data.json", 'w') as data:
                json.dump(self.data, data, indent=4)

    def rain_alert(self):
        self.check_data_relevance()

        print("checking the weather...\n")
        bring_an_umbrella = False
        for item in self.weather_for_21h:
            if item["weather"][0]["id"] < 700:
                bring_an_umbrella = True
        if bring_an_umbrella:
            message = self.client.messages.create(
                body="It would be bad weather today. Take an umbrella",
                from_=os.getenv("VIRTUAL_PHONE"),
                to=os.getenv("SEND_TO"),
            )


if __name__ == '__main__':
    app = RainAlertAPP()
