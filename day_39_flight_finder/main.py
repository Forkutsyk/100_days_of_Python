from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data_obj = DataManager()
flight_search_obj = FlightSearch()
flight_data_obj = FlightData()
sheet_data = data_obj.data

London_IATA = 'LON'
# Origin_IATA = flight_search_obj.get_iata("London") < ---- if i want the different city

for row in sheet_data:
    print(f"Getting flies for {row['city']} ... ")
    result = flight_search_obj.get_flight_data(London_IATA, row['iataCode'])
    print(f"{row['city']}: £{flight_data_obj.chepest_price(result)}\n")



print("Updates completed successfully!")
