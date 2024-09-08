import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from tkinter import *

load_dotenv("../.env")
TOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = os.getenv("PIXELA_USERNAME")
GRAPH = os.getenv("GRAPH_ID")


class HabitTracker:
    def __init__(self):
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.graph_endpoint = f"{self.pixela_endpoint}/{USERNAME}/graphs"
        self.pixel_endpoint = f"{self.pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

        self.user_parameters = {
            "token": TOKEN,
            "username": USERNAME,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }
        self.graph_parameters = {
            "id": GRAPH,
            "name": "Reading Graph",
            "unit": "pages",
            "type": "int",
            "color": "shibafu",
        }
        self.headers = {
            "X-USER-TOKEN": TOKEN
        }

    def add_pixel(self):
        today = datetime.now().strftime("%Y%m%d")
        data = {
            "date": today,
            "quantity": "5"
        }
        # print(self.pixel_endpoint)
        response = requests.post(url=self.pixel_endpoint, json=data, headers=self.headers)
        print(response.text)


if __name__ == '__main__':
    app = HabitTracker()
    # app.add_pixel()
