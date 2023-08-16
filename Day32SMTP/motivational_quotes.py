import smtplib
import datetime as dt
import random

MY_EMAIL = "prince.agyei.tuffour@gmail.com"
MY_PASSWORD = "enyjxmgfytityizn"

weekdays = {0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday"}

with open("quotes.txt", "r") as quotes_file:
    quotes_list = quotes_file.readlines()

now = dt.datetime.now()

if now.weekday() in weekdays:
    quote = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # transfer layer security for email encryption
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="nanakwameagyeituffour@gmail.com",
            msg=f"Subject:{weekdays[now.weekday()]} Motivation\n\n"
                f"{quote}"
        )
