import smtplib
import global_variables
import random
from datetime import date

MY_EMAIL = "elitas2003@gmail.com"
PASSWORD = "password..."
MESSAGE = random.choice(global_variables.birthday_wishes)
today = date.today()

if today == any(global_variables.birthday_dates):
    print("true")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="elitas2003@gmail.com",
            msg=MESSAGE
        )
else:
    print("Date selected:",global_variables.birthday_dates)