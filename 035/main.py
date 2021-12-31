import requests
import os
from twilio.rest import Client

def is_umbrella_needed(id):
    if id < 700:
        umbrella_needed = True
    else:
        umbrella_needed = False
    return umbrella_needed

def check_weather_data_if_umbrella_needed(weather_data):
    umbrella_needed = False
    next_12_hr_weather_data = weather_data.get("hourly")[0:12]
    for hourly_data in next_12_hr_weather_data:
        weather = hourly_data.get("weather")
        for weather_condition in weather:
            weather_id = int(weather_condition.get("id"))
            if is_umbrella_needed(weather_id):
                umbrella_needed = True
    return umbrella_needed

def send_sms_alert():
    to_number = os.environ["TWILIO_TO_PHONE_NUMBER"]
    from_number = os.environ["TWILIO_FROM_PHONE_NUMBER"]
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="It will rain today, bring an umbrella with you!",
                        from_=f"+{from_number}",
                        to=f"+{to_number}"
                    )
    print(message.status)

api_key = os.getenv("API_KEY")

if not api_key:
    api_key = input("Enter API key: ")

endpoint = "https://api.openweathermap.org/data/2.5/onecall"
params = {
    "lat": 51.500153,
    "lon": -0.1262362,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(url=endpoint, params=params)
response.raise_for_status()

weather_data = response.json()

if check_weather_data_if_umbrella_needed(weather_data):
    print("bring an umbrella!")
    if os.getenv("TWILIO_ACCOUNT_SID") != None and os.getenv("TWILIO_AUTH_TOKEN") != None and os.getenv("TWILIO_TO_PHONE_NUMBER") != None and os.getenv("TWILIO_FROM_PHONE_NUMBER") != None:
        send_sms_alert()
