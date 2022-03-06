import smtplib
import global_variables
import random
import datetime as dt

MY_EMAIL = "elitas2003@gmail.com"
PASSWORD = "nr20031107"
MESSAGE = random.choice(global_variables.quotes)

if dt.date.today().isoweekday() == 7:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="elitas2003@gmail.com",
            msg=MESSAGE
        )
