import smtplib
import getpass
import datetime as dt
import os
import random

now = dt.datetime.now()
directory = os.path.realpath(__file__ + f"/{os.pardir}")
quote_file = f"{directory}/quotes.txt"

if now.weekday() == 0:
    my_email = input("Email address: ")
    password = getpass.getpass()
    to_address = input("Who to sent email to: ")

    with open(quote_file) as f:
        quotes = f.read().splitlines()
    quote_of_the_day = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_address,
            msg=f"Subject:Monday Motivation E-mail\n\n{quote_of_the_day}"
        )