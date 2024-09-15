import requests
from dotenv import load_dotenv
import os
from datetime import datetime as dt
from requests.auth import HTTPBasicAuth

load_dotenv("../.env")
TODAY_DATE = dt.now().date().strftime("%d/%m/%Y")
TIME = dt.now().time().strftime("%H:%M:%S")
basic = HTTPBasicAuth(os.getenv("NUTRISION_USER"), os.getenv("NUTRISION_PASSWORD"))


def updating_the_sheet(exercise, duration, calories):
    sheety_url = 'https://api.sheety.co/9abc1aef616607b7b1ba85a3e8626de7/workoutTracking/workouts'
    new_data = {
        'workout': {
            'date': TODAY_DATE,
            'time': TIME,
            'exercise': exercise,
            'duration': duration,
            'calories': calories,
        }
    }
    sheety_response = requests.post(url=sheety_url, json=new_data, auth=basic)
    sheety_response.raise_for_status()
    return sheety_response


def taking_the_data():
    user_input = input("Tell me which exercise you did: ")

    app_id = os.getenv("NUTRITION_APP_ID")
    app_key = os.getenv("NUTRITION_APP_KEY")
    workout_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

    headers = {
        'Content-Type': 'application/json',
        'x-app-id': app_id,
        'x-app-key': app_key,
    }
    options = {
        "query": user_input,
    }
    response = requests.post(url=workout_url, json=options, headers=headers)
    response.raise_for_status()

    data = response.json()['exercises']
    data_n = {}
    for i in data:
        data_n[data.index(i)] = {
                                 'exercise': i['name'],
                                 'duration': i['duration_min'],
                                 'calories': i['nf_calories'],
                                 }
    return data_n


def main_logic():
    data = taking_the_data()
    for i in data:
        response = updating_the_sheet(data[i]['exercise'], data[i]['duration'], data[i]['calories'])
        # print(response.text)


if __name__ == '__main__':
    main_logic()

# Should i try to rewrite it in the Class structure ? Or just to fix small bugs ?
