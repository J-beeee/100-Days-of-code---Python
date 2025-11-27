import smtplib
import datetime as dt
import random

my_mail = "insert email here"
password = "insert password here"
now = dt.datetime.now()
day = now.weekday()

if day == 3:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        with open("quotes.txt") as data:
            quote_list = data.readlines()
            random_quote = random.choice(quote_list)
        connection.sendmail(from_addr=my_mail, to_addrs="insert email here", msg=f"Subject:Thursday Motivation\n\n{random_quote}")
    print(f"Email send! Quote: {random_quote}")