from twilio.rest import Client
import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, account_sid, auth_token, from_number, smtp_from_address, smtp_password) -> None:
        self.from_number = from_number
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.smtp_from_address = smtp_from_address
        self.smtp_password = smtp_password
        self.client = Client(account_sid, auth_token)

    def send_sms_notification(self, notification, to_number):
        self.client.messages.create(
            body=notification,
            from_=f"+{self.from_number}",
            to=f"+{to_number}"
        )

    def send_email_notification(self, notification, to_address):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.smtp_from_address, password=self.smtp_password)
            connection.sendmail(
                from_addr=self.smtp_from_address,
                to_addrs=to_address,
                msg=f"Subject:Flight club deals\n\n{notification}".encode('utf-8')
            )
