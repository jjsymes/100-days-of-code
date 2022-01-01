import requests
import datetime as dt

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    TEQUILA_API_ENDPOINT = "https://tequila-api.kiwi.com"

    def __init__(self, tequila_api_key) -> None:
        self.tequila_api_key = tequila_api_key
        self.header = {
            "apikey": self.tequila_api_key
        }

    def get_iata_code(self, city):
        endpoint = f"{self.TEQUILA_API_ENDPOINT}/locations/query"
        request_params = {
            "term": city,
            "locale": "en-US",
            "location_types": "city",
            "limit": 1,
            "active_only": True
        }
        req = requests.get(endpoint, params=request_params, headers=self.header)
        req.raise_for_status()
        return req.json()["locations"][0]["code"]

    def search_flights(self, fly_from, fly_to, max_price):
        now = dt.datetime.now()
        date_from = (now + dt.timedelta(days=1)).strftime("%d/%m/%Y")
        date_to = (now + dt.timedelta(days=183)).strftime("%d/%m/%Y")
        endpoint = f"{self.TEQUILA_API_ENDPOINT}/v2/search"
        request_params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "dateFrom": date_from,
            "dateTo": date_to,
            "price_to": int(max_price),
            "limit": 1,
            "flight_type": "round",
            "nights_in_dst_from": 2,
            "nights_in_dst_to": 30,
            "curr": "GBP",
        }
        req = requests.get(endpoint, params=request_params, headers=self.header)
        req.raise_for_status()
        return req.json()
