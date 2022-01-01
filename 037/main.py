import requests
from datetime import datetime
import getpass

USERNAME = "jjs"
TOKEN = getpass.getpass("Enter auth token: ")
GRAPH_ID = "test-graph"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

## POST
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "graph-name",
    "unit": "commit",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()
today_formatted = today.strftime("%Y%m%d")

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many (int)? "),
}

response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today_formatted}"

new_pixel_data = {
    "quantity": "2401"
}

## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today_formatted}"

## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
