import smtplib

my_email = "callme.bhawesh@yahoo.com"
my_password = "jdeikinititlonlj"

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="kaflekushal5@gmail.com",
        msg="Subject:Testing\n\nThis is an automated python code to send emails."
    )