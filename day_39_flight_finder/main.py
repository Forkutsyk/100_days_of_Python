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
notifier = NotificationManager()

tomorrow = (datetime.today() + timedelta(days=1))
six_month = (datetime.today() + timedelta(days=6*30))


# Origin_IATA = flight_search_obj.get_iata("London") < ---- if I want the different city

for destination in sheet_data:
    print(f"Getting flies for {destination['city']} ...")
    data = flight_search_obj.get_flight_data(
        ORIGIN_CITY_IATA,
        destination['iataCode'],
        from_date=tomorrow,
        to_date=six_month
    )
    cheapest_flight = flight_data.cheapest_price(data)
    # # the twilio package does not work on the laptop , I should check on the PC
    # but everything beside notification is working okay
    if cheapest_flight.price < destination['lowestPrice']:
        notifier.send_notification(
            cheapest_flight.price,
            cheapest_flight.origin_airport,
            cheapest_flight.destination_airport,
            cheapest_flight.out_date,
            cheapest_flight.return_date,
        )
        print("Notification sent!")
    else:
        print(f"Nothing to notify for {destination['city']}\n")
    # Slowing down requests to avoid rate limit
    time.sleep(2)


print("Updates completed successfully!")
