import os
from dotenv import load_dotenv
import requests
from datetime import datetime,timedelta

load_dotenv("../.env")
TOMORROW = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
SIX_MONTH = (datetime.today() + timedelta(days=180)).strftime("%Y-%m-%d")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._apikey = os.environ["AMADEUS_KEY"]
        self._api_secret = os.environ['AMADEUS_SECRET']
        self._token = self._get_new_token()
        self.headers = {
            'Authorization': f'Bearer {self._token["access_token"]}'
        }

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
        return response.json()

    def get_iata(self, city_name):
        amadeus_endpoint = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'

        params = {
            'keyword': city_name.upper()
        }
        amadeus_response = requests.get(url=amadeus_endpoint, headers=self.headers, params=params)
        amadeus_response.raise_for_status()  # Will raise an error if the response is not 2xx
        return amadeus_response.json()['data'][0]['iataCode']

    def get_flight_data(self, origin, destination):
        endpoint = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
        params = {
            'originLocationCode': origin,
            'destinationLocationCode': destination,
            'departureDate': (TOMORROW,SIX_MONTH),
            'adults': 1,
            'nonStop': 'true',
            'currencyCode': 'GBP',
        }

        response = requests.get(url=endpoint, headers=self.headers, params=params)
        # print("Response Status Code:", response.status_code)
        if response.status_code == 204:  # No content, skip gracefully
            return None
        response.raise_for_status()
        return response.json()
