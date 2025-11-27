import smtplib
import datetime as dt
import random
import pandas as pd

data = pd.read_csv("birthdays.csv")

now = dt.datetime.now()
month = now.month
day = now.day
i = 0
month_data = data["month"]
day_data = data["day"]
email_data = data.email
has_birthday = ""
for i in range(len(data)):
    if month_data[i] == month:
            if day_data[i] == day:
                has_birthday = data.iloc[i]
            random_number = random.randint(1,3)
            file = fr"letter_templates\letter_{random_number}.txt"
            with open(file, "r") as mail:
                mail = mail.read()
                mail = mail.replace("[NAME]", has_birthday["name"])
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user="test",password="test")
                connection.sendmail(from_addr="test",to_addrs=data.email[i],msg=f"SUBJECT:Happy Birthday\n\n{mail}")
    i += 1





