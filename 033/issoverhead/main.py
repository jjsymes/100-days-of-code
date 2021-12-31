import requests
from datetime import datetime
from time import sleep
import getpass
import smtplib
import config

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

sender_email = config.email
if not sender_email:
    sender_email = input("Email address: ")
recipient_email = sender_email
password = config.password
if not password:
    password = getpass.getpass()

def send_notification():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=recipient_email,
            msg=f"Subject:ISS is overhead, look up!\n\nISS is overhead, look up!\nTime: {time_now}\nISS latitude: {iss_latitude}\nISS longitude: {iss_longitude}"
        )


def is_iss_overhead():
    lat_difference = MY_LAT - iss_latitude
    long_difference = MY_LONG - iss_longitude
    if lat_difference < 5 and lat_difference > -5 and long_difference < 5 and long_difference > -5:
        overhead = True
    else:
        overhead = False
    return overhead


def is_dark():
    hour = time_now.hour
    if hour < sunrise or hour > sunset:
        dark = True
    else:
        dark = False
    return dark


def notify_if_iss_visible():
    if is_iss_overhead() and is_dark():
        send_notification()
    sleep(60)
    notify_if_iss_visible()


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

notify_if_iss_visible()
