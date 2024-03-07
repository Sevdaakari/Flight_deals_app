import requests

SHEETY_ENDPOINT = "https://api.sheety.co/429eba0ff7dc7c3ea23346a60c4c9e4e/flightDealsSevda/prices"
USERS_ENDPOINT = "https://api.sheety.co/429eba0ff7dc7c3ea23346a60c4c9e4e/flightDealsSevda/users"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, verify=False).json()
        self.destination_data = response["prices"]
        return self.destination_data

    def destination_update(self):
        for city in self.destination_data:
            updated_row = {
                "price": {
                  "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", verify=False, json=updated_row)
            return response

    def get_user_data(self):
        self.user_data = requests.get(url=USERS_ENDPOINT, verify=False).json()["users"]
        return self.user_data


