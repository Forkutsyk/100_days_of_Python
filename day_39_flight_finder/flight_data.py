

class FlightData:
    def chepest_price(self, respond):
        prices = []
        for i in respond['data']:
            prices.append(float(i['price']['total']))
        # print(prices)
        return min(prices)
