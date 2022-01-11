import smtplib
import datetime as dt
import random

MY_EMAIL = "callme.bhawesh@yahoo.com"
PASSWORD = "your_password"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="kaflekushal5@gmail.com",
                            msg=f"Subject: Tuesday Motivation\n\n{quote}")