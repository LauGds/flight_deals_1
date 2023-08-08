import requests

USER = "<<USER>>"
PASS = "<<PASSWORD>>"
sheet_endpoint = "https://api.sheety.co/98b013e70fc6560bb992a4610bca2509/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheet_endpoint, auth=(USER, PASS))
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheet_endpoint}/{city['id']}",
                json=new_data,
                auth=(USER, PASS)
            )
            print(response.text)
