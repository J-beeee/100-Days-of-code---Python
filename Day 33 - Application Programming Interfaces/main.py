import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 52.3730944
MY_LONG = 14.0836864
def check_iss_over_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    range_iss_latitude = (iss_latitude - 5, iss_latitude + 5)
    range_iss_longitude = (iss_longitude -5, iss_longitude +5)
    if range_iss_longitude[0] <= MY_LONG <= range_iss_longitude[1] and range_iss_latitude[0] <= MY_LAT <= range_iss_latitude[1]:
        return True
    return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    hour_now = time_now.hour
    if sunset <= hour_now  or  hour_now <= sunrise:
        return True
    return False

while True:
    time.sleep(60)
    if is_night() and check_iss_over_me():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="test", password="test")
            connection.sendmail(from_addr="test", to_addrs="test", msg="Subject:Look up\n\nThe ISS is over u!")







