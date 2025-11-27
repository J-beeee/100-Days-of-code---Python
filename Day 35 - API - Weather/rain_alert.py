import requests
from twilio.rest import Client

OMW_Endpoint = r"https://api.openweathermap.org/data/2.5/forecast"
api_key = "Your Api key"

account_sid = "Your SID"
auth_token = "Your token"



weather_params = {
    "lat": 52.17011760103034,
    "lon": 14.246860768879817,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=OMW_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
list = weather_data["list"]

rain = False
for item in list:
    if int(item["weather"][0]["id"]) < 700:
        rain = True
if rain:
    print("It may rain.")
    client = Client(account_sid, auth_token)

    message = client.api.account.messages.create(
        to="to number",
        from_="sender number",
        body="It may rain.")
    print(message.status)