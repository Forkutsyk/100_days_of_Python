import os
from dotenv import load_dotenv
import requests

load_dotenv("../.env")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._apikey = os.environ["AMADEUS_KEY"]
        self._api_secret = os.environ['AMADEUS_SECRET']
        self._token = self._get_new_token()

    # Function to get a new token for work with Amadeus API
    def _get_new_token(self):
        token_endpoint = 'https://test.api.amadeus.com/v1/security/oauth2/token'
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._apikey,
            'client_secret': self._api_secret
        }
        response = requests.post(url=token_endpoint, headers=header, data=body)
        print(f"Your token expires in {response.json()['expires_in']} seconds\n")
        return response.json()["access_token"]

    # Func to get the IATA code for the country mentioned in Google sheet
    def get_iata(self, city_name):
        endpoint = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'
        headers = {'Authorization': f'Bearer {self._token}'}
        params = {
            'keyword': city_name.upper()
        }
        amadeus_response = requests.get(url=endpoint, headers=headers, params=params)
        amadeus_response.raise_for_status()  # Will raise an error if the response is not 2xx
        return amadeus_response.json()['data'][0]['iataCode']

    # Func to get information about the flights to the countries mentioned in the sheet
    def get_flight_data(self, origin, destination, from_date, to_date):
        endpoint = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
        headers = {'Authorization': f'Bearer {self._token}'}
        params = {
            'originLocationCode': origin,
            'destinationLocationCode': destination,
            "departureDate": from_date.strftime("%Y-%m-%d"),
            "returnDate": to_date.strftime("%Y-%m-%d"),
            'adults': 1,
            'nonStop': 'true',
            'currencyCode': 'GBP',
            "max": "20"
        }

        response = requests.get(url=endpoint, headers=headers, params=params)
        # print("Response Status Code:", response.status_code)
        if response.status_code != 200:
            print(f"get_flight_data() response code: {response.status_code}")
            print(response.text)
            return None

        response.raise_for_status()
        return response.json()
