from datetime import datetime

import os
import requests

APP_ID = os.environ.get("APP_ID", "Env variable does not exist")
API_KEY = os.environ.get("API_KEY", "Env variable does not exist")
TOKEN = os.environ.get("TOKEN", "Env variable does not exist")

GENDER = "male"
WEIGHT_KG = 91
HEIGHT_CM = 180.57
AGE = 25

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ.get("SHEETY_ENDPOINT", "Env variable does not exist")
exercise_text = input("Tell me what exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

headers = {
    "Authorization": f"Bearer {TOKEN}",
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=headers)

    print(sheet_response.text)
