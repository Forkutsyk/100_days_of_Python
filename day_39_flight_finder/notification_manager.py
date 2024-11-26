import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client
import smtplib

load_dotenv("../.env")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.getenv("PHONE_NUMBER_SID")
        self.auth_token = os.getenv("AUTH_PHONE_TOKEN")
        self.client = Client(self.account_sid, self.auth_token)
        self.MY_EMAIL = os.getenv("MY_EMAIL")
        self.PASSWORD = os.getenv("MY_EMAIL_PASSWORD")
        self.SENT_TO = os.getenv("SENT_TO")

    def direct_check(self, stops):
        if stops > 1:
            return f"with only {stops} stops."
        else:
            return "which is direct."

    def send_notification(self, price, fly_from, fly_to, flight_date, arrival_date, stops):
        message = self.client.messages.create(
            body=f"Low price alert!Only £{price} to fly from {fly_from} to {fly_to},on {flight_date} until {arrival_date} {self.direct_check(stops)}",
            from_=os.getenv("VIRTUAL_PHONE"),
            to=os.getenv("SEND_TO"),
        )

    def inform_users(self, price, fly_from, fly_to, flight_date, arrival_date, stops, user):

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.MY_EMAIL, password=self.PASSWORD)
            subject = "Low Price Alert!"
            body = f"Low price alert! Only GBP{price} to fly from {fly_from} to {fly_to}, on {flight_date} until {arrival_date} {self.direct_check(stops)}"
            msg = f"Subject: {subject}\n\n{body}"


            connection.sendmail(
                from_addr=self.MY_EMAIL,
                to_addrs=user,
                msg=msg
            )

    # print("inform_users() sent")
