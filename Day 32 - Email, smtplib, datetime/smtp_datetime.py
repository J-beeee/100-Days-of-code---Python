import smtplib
import datetime as dt

my_mail = "test"
password = "test"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(
        from_addr=my_mail,
        to_addrs="test",
        msg="Subject:Hello\n\nThis is the body of my email"
    )

now = dt.datetime.now()
now = now.year
print(now)
date_of_brith = dt.datetime(year=1991, month=11, day=11)
print(date_of_brith)