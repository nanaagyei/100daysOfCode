import requests
from datetime import datetime


USERNAME = "nanakwame"
USER_TOKEN = "thisismytoken"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": USER_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": GRAPH_ID,
    "name": "Personal Coding Tracker",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": USER_TOKEN
}
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)
today = datetime(year=2023, month=12, day=30)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "80",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_config = {
    "quantity": "105",
}

# response = requests.delete(url=pixel_update_endpoint, headers=headers)
# print(response.text)
# TODO: Modify to make it more user-friendly with Tkinter.
# TODO: (Optional) Make it a web-based with Flask

