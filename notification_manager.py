import os
import smtplib

from twilio.rest import Client
from flight_search import FlightSearch


TWILIO_SID = "ACd4eedc9dedda5457c6a9fe34b36e6f66"
TWILIO_TOKEN = "1c93c559314aaf47bd8113a5f1f1d736"
TWILIO_NUMBER = "+15178169617"


class NotificationManager:
    def send_message(self, message):
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        message = client.messages.create(body=message,
        from_=TWILIO_NUMBER, to="+48516033828")
        print(message.sid)

    def send_mail(self, client, mail, link):
        my_mail = "sevdapycharm@gmail.com"
        my_password = "ewhetdnlzldocpdw"
        # "jsryepxxfiosbcnf"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail, password=my_password)
            connection.sendmail(from_addr=my_mail, to_addrs=client,
                                msg=f"Subject: Here is the low cost flight!\n\n {mail}\n{link}".encode('utf-8'))


