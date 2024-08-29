import requests
from datetime import datetime as dt
from time import sleep
import smtplib
import os
from dotenv import load_dotenv

# My current position
LAT = 50.064651
LNG = 19.944981
SLEEP_TIME = 60
time_now = dt.now().hour
load_dotenv("../.env")
MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("MY_EMAIL_PASSWORD")


def get_iss_position():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    data_iss = iss_response.json()

    iss_latitude = float(data_iss['iss_position']['latitude'])
    iss_longitude = float(data_iss['iss_position']['longitude'])
    print(f"ISS Position: {iss_latitude}; {iss_longitude}\n Your: {LAT}; {LNG}")
    return iss_latitude, iss_longitude


def get_sunset_sunrice_time():
    response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={LAT}&lng={LNG}&formatted=0")
    response.raise_for_status()

    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(":")[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(":")[0])
    return sunrise, sunset


def send_mail(lat, lng):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:ISS Overhead !!!\n\nISS overhead ! At: {lat}; {lng};")
        connection.close()


def main_logic(sunrise, sunset):
    iss_latitude, iss_longitude = get_iss_position()

    if time_now >= sunset or time_now <= sunrise:
        lat_check = LAT - 5 <= iss_latitude <= LAT + 5
        lng_check = LNG - 5 <= iss_longitude <= LNG + 5
        if lat_check and lng_check:
            send_mail(iss_latitude, iss_longitude)
    else:
        print("not now")
    pass


if __name__ == '__main__':
    my_location_sunrise, my_location_cracow_sunset = get_sunset_sunrice_time()
    while True:
        main_logic(my_location_sunrise, my_location_cracow_sunset)
        sleep(SLEEP_TIME)
