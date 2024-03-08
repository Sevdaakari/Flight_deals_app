import os
import smtplib

from twilio.rest import Client
from flight_search import FlightSearch


TWILIO_SID = "twilio_sid"
TWILIO_TOKEN = "twilio_token"
TWILIO_NUMBER = "my_twilio_number"


class NotificationManager:
    def send_message(self, message):
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        message = client.messages.create(body=message,
        from_=TWILIO_NUMBER, to="my_phone_number")
        print(message.sid)

    def send_mail(self, client, mail, link):
        my_mail = "mymail@gmail.com"
        my_password = "here_is_my_password"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail, password=my_password)
            connection.sendmail(from_addr=my_mail, to_addrs=client,
                                msg=f"Subject: Here is the low cost flight!\n\n {mail}\n{link}".encode('utf-8'))


