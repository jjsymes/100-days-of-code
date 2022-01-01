import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, sheety_endpoint, sheety_access_token) -> None:
        self.sheety_endpoint =  sheety_endpoint
        self.sheety_access_token = sheety_access_token
        self.sheety_header = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.sheety_access_token}"
        }

    def get_sheet_data(self, sheet):
        url = f"{self.sheety_endpoint}/{sheet}"
        req = requests.get(url, headers=self.sheety_header)
        req.raise_for_status()
        return req.json()

    def edit_sheet_row(self, sheet, object_id, data):
        url = f"{self.sheety_endpoint}/{sheet}/{object_id}"
        req = requests.put(url, data=data, headers=self.sheety_header)
        req.raise_for_status()
        return req.json()
