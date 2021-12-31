import smtplib
import getpass

my_email = input("Email address: ")
password = getpass.getpass()
to_address = input("Who to sent email to: ")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_address,
        msg="Subject:Test E-mail\n\nHello World!"
    )