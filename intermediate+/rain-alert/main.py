import requests
import os
from twilio.rest import Client

LATITUDE = 47.56263
LONGITUDE = 19.11681
API_KEY = os.environ.get("OWM_API_KEY")
account_sid = "AC6297a1e76f4b220eb88560885ca1baf8"
auth_token = os.environ.get("API_KEY")


parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts",
}

response = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
next_12_hours = weather_data["hourly"][:12]

will_rain = False
for hour in next_12_hours:
    if hour["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+13083373817',
        body='It will rain today. Do not forget to bring an umbrella!',
        to='+36302304217'
    )

