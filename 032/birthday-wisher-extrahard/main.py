##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import os
import datetime as dt
import smtplib
import getpass
import random

my_email = input("Email address: ")
password = getpass.getpass()

directory = os.path.realpath(__file__ + f"/{os.pardir}")

current_date = dt.datetime.now()
month = current_date.month
day = current_date.day

directory = os.path.realpath(__file__ + f"/{os.pardir}")
birthday_file = f"{directory}/birthdays.csv"

birthday_data = pandas.read_csv(birthday_file)

current_birthdays = birthday_data.loc[birthday_data["month"] == month] \
                                 .loc[birthday_data["day"] == day]

for idx, row in current_birthdays.iterrows():
    email = row["email"]
    name = row["name"]

    random_letter_file = f"letter_{random.randint(1, 3)}.txt"
    with open(f"{directory}/letter_templates/{random_letter_file}") as f:
        template = f.read()
    
    letter = template.replace("[NAME]", name)
    email_msg = f"Subject:Happy Birthday {name}!\n\n{letter}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=email_msg
        )
