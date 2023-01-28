import requests
import datetime as dt
import smtplib
import time

MY_LAT = 17.686815
MY_LONG = 83.218483
MY_EMAIL = "callme.bhawesh@yahoo.com"
RECEIVER_EMAIL = "kaflekushal5@gmail.com"
PASSWORD = "PASSWORD"


def is_iss_overhead():
    response = requests.get(url="https://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()["iss_position"]
    longitude = data["longitude"]
    latitude = data["latitude"]
    iss_position = (longitude, latitude)

    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LONG - 5 <= longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = float(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = float(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.mail.yahoo.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=RECEIVER_EMAIL,
                            msg="Subject: ISS Overhead Notifier\n\nCheck Their is somewhere "
                                "internation space station over your head in the sky.")
