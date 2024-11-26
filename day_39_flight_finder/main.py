from data_manager import DataManager
from flight_search import FlightSearch
import flight_data
from datetime import datetime, timedelta
import time
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = 'LON'

data_obj = DataManager()
flight_search_obj = FlightSearch()
sheet_data = data_obj.data
users_data = data_obj.user_data
notifier = NotificationManager()

tomorrow = (datetime.today() + timedelta(days=1))
six_month = (datetime.today() + timedelta(days=6*30))


def sent_notification_sms(cheap_flight_alert):
    # notifier.send_notification(
    #     cheap_flight_alert.price,
    #     cheap_flight_alert.origin_airport,
    #     cheap_flight_alert.destination_airport,
    #     cheap_flight_alert.out_date,
    #     cheap_flight_alert.return_date,
    #     cheap_flight_alert.nr_stops)
    print("Notification sent!")


def notify_users(cheap_flight_alert, user_email):

    notifier.inform_users(
        cheap_flight_alert.price,
        cheap_flight_alert.origin_airport,
        cheap_flight_alert.destination_airport,
        cheap_flight_alert.out_date,
        cheap_flight_alert.return_date,
        cheap_flight_alert.nr_stops,
        user_email)
    print(f"\n user {user_email}  notified!")

# ORIGIN_CITY_IATA = flight_search_obj.get_iata("London") < ---- if I want the different city


for destination in sheet_data:
    print(f"Getting direct flies for {destination['city']} ...")
    data = flight_search_obj.get_flight_data(
        ORIGIN_CITY_IATA,
        destination['iataCode'],
        from_date=tomorrow,
        to_date=six_month
    )
    cheapest_flight = flight_data.cheapest_price(data)
    # # the twilio package does not work on the laptop , I should check on the PC
    # but everything beside notification is working okay
    if data is not None and cheapest_flight.price < destination['lowestPrice']:
        sent_notification_sms(cheapest_flight)
        for user in users_data:
            notify_users(cheapest_flight, user)

    elif data is None:
        print("No direct flights found, searching for indirect flights")
        data = flight_search_obj.get_flight_data(
            ORIGIN_CITY_IATA,
            destination['iataCode'],
            from_date=tomorrow,
            to_date=six_month,
            is_direct='false'
        )
        cheapest_flight = flight_data.cheapest_price(data)
        sent_notification_sms(cheapest_flight)
        for user in users_data:
            notify_users(cheapest_flight, user)

    # else:
    #     print("Nothing to notify.")

    # Slowing down requests to avoid rate limit
    time.sleep(2)


print("\nUpdates completed successfully!")
