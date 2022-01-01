from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, account_sid, auth_token, from_number) -> None:
        self.from_number = from_number
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.client = Client(account_sid, auth_token)

    def send_sms_notification(self, notification, to_number):
        self.client.messages.create(
            body=notification,
            from_=f"+{self.from_number}",
            to=f"+{to_number}"
        )
