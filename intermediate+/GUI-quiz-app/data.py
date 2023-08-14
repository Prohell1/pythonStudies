import requests


questions_api = requests.get("https://opentdb.com/api.php?amount=10&category=31&type=boolean").json()

question_data = questions_api["results"]
