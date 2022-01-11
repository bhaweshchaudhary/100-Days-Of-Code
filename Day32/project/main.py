import smtplib
import pandas
import datetime as dt

MY_EMAIL = "callme.bhawesh@yahoo.com"
PASSWORD = "password"

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")

# Dictionary comprehension template for pandas Dataframe looks like this:
# new_dict = {new_key:new_value for (index, data_row) in data.iterrows()}

birthday_dict = {(data_row.month, data_row.day):data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    letter_path = "text.txt"
    with open(letter_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person.email, msg=f"Subject: Happy Birthday\n\n{contents}")