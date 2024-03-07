import requests
from datetime import datetime
from datetime import timedelta
from flight_data import FlightData
from pprint import pprint

API_KEY = "my_api_key"
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"

HEADERS = {"apikey": API_KEY}

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def find_city_code(self, city_name):
        Params = {
            "term": city_name,
            "location_types": "city",
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=HEADERS, params=Params,
                                verify=False).json()["locations"][0]["code"]
        return response

    def show_city_data(self, from_city_code, to_city_code, from_time, to_time):
        params = {
            "fly_from": from_city_code,
            "fly_to": to_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 5,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
}
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=HEADERS,
                                params=params, verify=False).json()
        try:
            flights = response["data"][0]

        except IndexError:
            params["max_stopovers"] = 1
            response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=HEADERS,
                                    params=params, verify=False).json()
            try:
                flights = response["data"][0]

            except IndexError:
                return None
            else:
                flight_data = FlightData(price=flights["price"], from_city=flights["route"][0]["cityFrom"],
                                      from_airport=flights["route"][0]["flyFrom"],
                                      to_city=flights["route"][1]["cityTo"],
                                      to_airport=flights["route"][1]["flyTo"],
                                      flight_date=flights["route"][0]["local_departure"].split("T")[0],
                                      return_date=flights["route"][2]["local_departure"].split("T")[0],
                                      stop_overs=1, via_city=flights["route"][0]["cityTo"])
                print(f"flights: {flights}")
                print(f"To city: {flight_data.to_city}")
                return flight_data

        else:
            flight_data = FlightData(price=flights["price"], from_city=flights["route"][0]["cityFrom"],
                                     from_airport=flights["route"][0]["flyFrom"],
                                     to_city=flights["route"][0]["cityTo"],
                                     to_airport=flights["route"][0]["flyTo"],
                                     flight_date=flights["route"][0]["local_departure"].split("T")[0],
                                     return_date=flights["route"][1]["local_departure"].split("T")[0])
            print(f"flights: {flights}")
            print(f"To city: {flight_data.to_city}")
            return flight_data




