import requests
import os

FLIGHT_DEAL_SHEET_ENDPOINT = "https://api.sheety.co/5e896975398d618be7847043dec004ed/flightDeals/prices"
TOKEN = os.environ.get("TOKEN")
headers = {
    "Authorization": f"Bearer {TOKEN}"
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.response_data = {}

    def get_sheet_data(self):
        response = requests.get(url=FLIGHT_DEAL_SHEET_ENDPOINT, headers=headers)
        self.response_data = response.json()['prices']
        return self.response_data

    def update_sheet_data(self):
        for row in self.response_data:
            sheet_input = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            response = requests.put(url=f"{FLIGHT_DEAL_SHEET_ENDPOINT}/{row['id']}", json=sheet_input, headers=headers)

