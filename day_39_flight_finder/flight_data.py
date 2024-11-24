class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


def cheapest_price(data):
    if data is None or not data['data']:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    first_flight = data['data'][0]
    flight_price = float(first_flight['price']['total'])
    origin_airport = first_flight['itineraries'][0]['segments'][0]['departure']['iataCode']
    destination_airport = first_flight['itineraries'][0]['segments'][0]['arrival']['iataCode']
    out_date = first_flight['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
    return_date = first_flight['itineraries'][1]['segments'][0]['departure']['at'].split('T')[0]

    for flight in data['data']:
        price = float(flight['price']['total'])
        if price < flight_price:
            flight_price = price
            origin_airport = flight['itineraries'][0]['segments'][0]['departure']['iataCode']
            destination_airport = flight['itineraries'][0]['segments'][0]['arrival']['iataCode']
            out_date = flight['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
            return_date = flight['itineraries'][1]['segments'][0]['departure']['at'].split('T')[0]

    cheapest_flight = FlightData(
        flight_price,
        origin_airport,
        destination_airport,
        out_date,
        return_date
    )
    return cheapest_flight
