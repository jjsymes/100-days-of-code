import os
import requests


SHEETY_ENDPOINT =  os.getenv("SHEETY_ENDPOINT")
SHEETY_ACCESS_TOKEN = os.getenv("SHEETY_ACCESS_TOKEN")


def get_email_input():
    email_valid = False
    while not email_valid:
        email = input("What is your email?\n")
        email_validation = input("Type your email again.\n")
        if email == email_validation:
            email_valid = True
    return email


def add_user(first_name, last_name, email):

    url = f"{SHEETY_ENDPOINT}/users"

    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {SHEETY_ACCESS_TOKEN}"
    }

    request_body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }
    req = requests.post(url, json=request_body, headers=header)
    req.raise_for_status()


print("Welcome to Josh's flight club.")
print("We find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = get_email_input()

try:
    add_user(first_name, last_name, email)
except Exception:
    print("Error adding you to the club :(")
else:
    print("You're in the club!")
