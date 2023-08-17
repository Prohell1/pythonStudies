import requests
from datetime import datetime

USERNAME = "prohell"
TOKEN = "qwejiqijqrtw"

pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# ------------------ https://pixe.la/v1/users/prohell/graphs/graph1.html ----------------- #

put_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime(year=2023, month=8, day=16)
# print(today.strftime("%Y%m%d"))

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "4",
}

response = requests.post(url=put_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
