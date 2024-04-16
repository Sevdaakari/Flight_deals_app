from data_manager import DataManager
import requests
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

USERS_ENDPOINT = "https://api.sheety.co/here_is_your_endpoint"
FROM_MY_CITY = "WRO"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
fl = FlightSearch()
notify = NotificationManager()


for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = fl.find_city_code(row["city"])
data_manager.destination_update()
sheet_data = data_manager.get_destination_data()

tomorrow = datetime.now() + timedelta(days=1)
after_6months = datetime.now() + timedelta(days=180)


for to_city in sheet_data:
    flight = fl.show_city_data(from_city_code=FROM_MY_CITY, to_city_code=to_city["iataCode"],
                                    from_time=tomorrow.strftime("%d/%m/%Y"),
                                    to_time=after_6months.strftime("%d/%m/%Y"))

    connect = ""
        # f"https://www.google.com/travel/flights?q=Flights%20to%20{flight.to_city}" \
        #       f"%20from%20{FROM_MY_CITY}%20on%20{flight.flight_date}" \
        #       f"%20through%20{flight.return_date}"


    if flight is None:
        continue

    if flight.price < to_city["lowestPrice"]:

        users = data_manager.get_user_data()
        emails = [row["email"] for row in users]

        notify.send_mail(client=emails, mail=f"Low price alert! Only {flight.price} EUR to fly "
                                        f"from {flight.from_city}-{flight.from_airport} "
                                        f"to {flight.to_city}-{flight.to_airport}, "
                                        f"from {flight.flight_date}"
                                        f" to {flight.return_date}."
                                        f"Do not miss this opportunity!", link=connect)

        if flight.stop_overs > 0:
            notify.send_mail(client=emails, mail=f"Low price alert! Only {flight.price} EUR to fly "
                                        f"from {flight.from_city}-{flight.from_airport} "
                                        f"to {flight.to_city}-{flight.to_airport}, "
                                        f"from {flight.flight_date}"
                                        f" to {flight.return_date}."
                                        f"Flight has {flight.stop_overs} via {flight.via_city}."
                                        f"Do not miss this opportunity!", link=connect)

def add_user_data(FIRST_NAME, LAST_NAME, USER_EMAIL):
    user_params = {
        "user": {
            "firstName": FIRST_NAME,
            "lastName": LAST_NAME,
            "email": USER_EMAIL
        }
    }
    response = requests.post(url=USERS_ENDPOINT, verify=False, json=user_params).json()
    return response


print("Welcome to AKARI's flight club!\nWe find the best flight deals and email you.")
FIRST_NAME = input("What is your first name?\n")
if FIRST_NAME != "":
    LAST_NAME = input("What is your last name? \n")
    if LAST_NAME != "":
        USER_EMAIL = input("Please enter your email.\n")
        if USER_EMAIL != "":
            check_mail = input("Please type your email again.\n")
            if USER_EMAIL == check_mail:
                print("Welcome! You're in the club now!")
                add_user_data(FIRST_NAME, LAST_NAME, USER_EMAIL)







