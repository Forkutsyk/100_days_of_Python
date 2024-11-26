import requests
import json
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv


load_dotenv("../.env")
basic = HTTPBasicAuth(os.getenv("NUTRISION_USER"), os.getenv("NUTRISION_PASSWORD"))


class DataManager:

    def __init__(self):
        self.data = self.get_data()
        self.user_data = self.get_user_data()
        # # I put data from the sheet to json file to work with them locally,
        # as the sheety API limited to 200 requests/month
        # try:
        #     with open("sheet_data.json", 'r') as data:
        #         print("reading the file....\n")
        #         self.data = json.load(data)
        #
        # except FileNotFoundError:
        #     with open("sheet_data.json", 'w') as data:
        #         print("creating the file...\n")
        #         self.data = self.get_data()
        #         json.dump(self.data, data, indent=4)

    # A function to pull data from the Google sheet
    def get_data(self):
        # This class is responsible for talking to the Google Sheet.
        sheety_url = 'https://api.sheety.co/9abc1aef616607b7b1ba85a3e8626de7/flightDeals/prices'
        sheety_response = requests.get(url=sheety_url, auth=basic)
        sheety_response.raise_for_status()
        return sheety_response.json()["prices"]

    # A func to update the IATA code for the countries mentioned in the google sheet
    def iata_code_update(self, data):
        # Loop through each row and send a PUT request to update it
        for row in data:
            # Construct the URL for the specific row using its ID
            row_id = row["id"]
            put_sheety_url = f"https://api.sheety.co/9abc1aef616607b7b1ba85a3e8626de7/flightDeals/prices/{row_id}"

            updated_row = {"price": {"iataCode": row["iataCode"]}}

            # Send the PUT request to update the specific row
            sheety_response = requests.put(url=put_sheety_url, json=updated_row, auth=basic)
            sheety_response.raise_for_status()  # Raise an error if the request fails
            print(f"Updated row {row_id}: {sheety_response.json()}")

    def get_user_data(self):
        # This class is responsible for talking to the Google Sheet.
        sheety_url = os.getenv("USERS_SHEET_GET")
        sheety_response = requests.get(url=sheety_url, auth=basic)
        sheety_response.raise_for_status()
        users = []
        for user in sheety_response.json()['users']:
            users.append(user['whatIsYourEmail?'].strip())
        # print(users)
        return users
