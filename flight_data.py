

class FlightData:

    def __init__(self, price, from_city, from_airport, to_city, to_airport, flight_date,
                 return_date, stop_overs=0, via_city=""):
        self.price = price
        self.from_city = from_city
        self.from_airport = from_airport
        self.to_city = to_city
        self.to_airport = to_airport
        self.flight_date = flight_date
        self.return_date = return_date

        self.via_city = via_city
        self.stop_overs = stop_overs




