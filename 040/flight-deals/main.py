#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
import os
import json

SHEETY_ENDPOINT =  os.getenv("SHEETY_ENDPOINT")
SHEETY_ACCESS_TOKEN = os.getenv("SHEETY_ACCESS_TOKEN")
TEQUILA_API_KEY =  os.getenv("TEQUILA_API_KEY")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")
TWILIO_TO_NUMBER = os.getenv("TWILIO_TO_NUMBER")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
SMTP_FROM_ADDRESS = os.getenv("SMTP_FROM_ADDRESS")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
ORIGIN_CITY_IATA = "LON"

data_manager = DataManager(SHEETY_ENDPOINT, SHEETY_ACCESS_TOKEN)
flight_search = FlightSearch(TEQUILA_API_KEY)
notification_manager = NotificationManager(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER, SMTP_FROM_ADDRESS, SMTP_PASSWORD)

data = data_manager.get_sheet_data("prices")
flight_data = [FlightData.from_dict(flight) for flight in data['prices']]

user_data = data_manager.get_sheet_data("users")
user_emails = [user['email'] for user in user_data['users']]

for flight in flight_data:
    if flight.iata_code == "":
        flight.iata_code = flight_search.get_iata_code(flight.city)
        data_manager.edit_sheet_row("prices", flight.id, json.dumps({"price": flight.to_dict()}))

    flight_search_result = flight_search.search_flights(ORIGIN_CITY_IATA, flight.iata_code, flight.lowest_price)
    notification = "Cheap flights\n\n"
    for trip in flight_search_result['data']:
        notification += (f"# Cheap flight #\n"
        f"From: {trip['cityFrom']}-{trip['flyFrom']}\n"
        f"To: {trip['countryTo']['name']} {trip['cityTo']}-{trip['flyTo']}\n"
        f"Date: from {trip['local_departure']} to {trip['route'][-1]['local_departure']}\n"
        f"Price: £{trip['price']}\n"
        f"Link: {trip['deep_link']}\n\n"
        )
    notification = notification.rstrip("\n")
    if flight_search_result['_results'] > 0:
        for user_email in user_emails:
            notification_manager.send_email_notification(notification, user_email)
