import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client


load_dotenv("../.env")


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.getenv("PHONE_NUMBER_SID")
        self.auth_token = os.getenv("AUTH_PHONE_TOKEN")
        self.client = Client(self.account_sid, self.auth_token)

    def send_notification(self, price, fly_from, fly_to, flight_date, arrival_date):
        message = self.client.messages.create(
            body=f"Low price alert!Only {price} to fly from {fly_from} to {fly_to},on {flight_date} until {arrival_date}.",
            from_=os.getenv("VIRTUAL_PHONE"),
            to=os.getenv("SEND_TO"),
        )
