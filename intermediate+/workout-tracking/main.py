import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
NUT_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
TOKEN = os.environ["TOKEN"]

exercises = input("Tell me which exercises you did: ")

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

params = {
    "query": exercises
}

response = requests.post(url=NUT_ENDPOINT, json=params, headers=header).json()

now = datetime.now()
today = now.strftime("%Y/%m/%d")
time = now.strftime("%H:%M:%S")

header = {
    "Authorization": TOKEN
}

for workout in response["exercises"]:
    body = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": workout["name"],
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"],
        }
    }
    requests.post(url=SHEETY_ENDPOINT, json=body, headers=header)

