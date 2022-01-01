import os
import requests
import datetime as dt

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_ACCESS_TOKEN = os.getenv("SHEETY_ACCESS_TOKEN")


def enter_workout_to_sheet(date, time, exercise, duration, calories):

    sheety_enpoint = SHEETY_ENDPOINT

    sheety_header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {SHEETY_ACCESS_TOKEN}"
    }

    sheety_request_body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": str(duration),
            "calories": str(calories)
        }
    }
    req = requests.post(sheety_enpoint, json=sheety_request_body, headers=sheety_header)
    req.raise_for_status()


exercise = input("Enter an exercise: ")

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

nutritionix_endpoint = " https://trackapi.nutritionix.com"
exercise_endpoint = f"{nutritionix_endpoint}/v2/natural/exercise"

request_body = {
    "query": exercise,
    "gender":"male",
    "weight_kg":81,
    "height_cm":175,
    "age": 28
}

req = requests.post(exercise_endpoint, json=request_body, headers=header)
exercises = req.json().get("exercises")

time = dt.datetime.now()
date_string = time.strftime("%Y/%m/%d")
time_string = time.strftime("%H:%M:%S")

for exercise in exercises:
    enter_workout_to_sheet(date_string, time_string, exercise["name"], exercise["duration_min"], exercise["nf_calories"])
