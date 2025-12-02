# -------------------------------- IMPORT --------------------------------#
import requests, datetime, os
# -------------------------------- Environment Variables --------------------------------#
env = os.environ
# -------------------------------- CONNECTION DATA Nutrition and Exercise API --------------------------------#
headers ={
    "x-app-id": env["X-APP-ID"],
    "x-app-key": env["X-APP-KEY"]
}
base_url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

# -------------------------------- EXERCISE DATA --------------------------------#
user_input = input("Tell me wich exercises you did: ")

params = {
    "query": user_input,
    "gender": "female",
    "weight_kg": 60,
    "height_cm": 178,
    "age": 34
}

response = requests.post(url=base_url, json=params, headers=headers)
response.raise_for_status()
result = response.json()
sport_type = result['exercises'][0]['name'].capitalize()
duration = result['exercises'][0]['duration_min']
calories = result['exercises'][0]['nf_calories']
time = datetime
today = time.datetime.today().strftime(format="%d/%m/%Y")
time = time.datetime.now().strftime("%H:%M:%S")

# -------------------------------- CONNECTION DATA SHEETY API  --------------------------------#
sheety_headers = {
    "Authorization": env["SHEETY_AUTHORIZATION"]
}
sheety_url = env["SHEETY_URL"]

sheety_get = requests.get(url=sheety_url, headers=sheety_headers)
sheety_get.raise_for_status()
sheety_result = sheety_get.json()

id = len(sheety_result["tabellenblatt1"]) + 1

sheety_params = {
    'tabellenblatt1': {
        'date': today,
        'time': time,
        'exercise': sport_type,
        'duration': duration,
        'calories': calories,
        'id': id
    }
}


sheety_post_row = requests.post(url=sheety_url, json=sheety_params, headers=sheety_headers)
sheety_post_row.raise_for_status()



