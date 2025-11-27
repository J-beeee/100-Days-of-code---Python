import requests
from datetime import datetime
#response = requests.get(url="http://api.open-notify.org/iss-now.json")
#response.raise_for_status()
#data = response.json()["iss_position"]["longitude"]
#print(data)
MY_LAT = 52.3730944
MY_LNG = 14.0836864
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)