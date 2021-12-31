import requests
import datetime as dt
import os
from twilio.rest import Client


STOCK = "INTC"
COMPANY_NAME = "Intel Corporation"
ALPHA_VANTAGE_API_KEY = os.environ["ALPHA_VANTAGE_API_KEY"]
NEWSAPI_API_KEY = os.environ["NEWSAPI_API_KEY"]
SENSITIVITY = 5


def get_stock_data():
    url = "https://www.alphavantage.co/query"

    params = {
        "apikey": ALPHA_VANTAGE_API_KEY,
        "symbol": STOCK,
        "function": "TIME_SERIES_DAILY"
    }
    r = requests.get(url, params=params)
    return r.json()


def get_news_data():
    url = "https://newsapi.org/v2/everything"

    params = {
        "apiKey": NEWSAPI_API_KEY,
        "sortBy": "relevancy",
        "q": COMPANY_NAME,
        "pageSize": 3,
        "language": "en"
    }
    r = requests.get(url, params=params)
    return r.json() 


def percentage_difference(num1, num2):
    return ((num1 - num2) / num1) * 100


def format_sms_notification(stock, stock_percentage_change, news_data):
    notification_body = f"{stock}: "
    if stock_percentage_change >= 0:
        notification_body += "🔺"
    else:
        notification_body += "🔻"
    notification_body += "{:.2f}".format(stock_percentage_change)
    notification_body += f"%\n\n"
    for article in news_data.get("articles"):
            notification_body += f"{article.get('title')}\n"
            notification_body += f"{article.get('description')}\n\n"
    notification_body = notification_body.rstrip("\n")
    return notification_body


def send_sms_notification(notification, to_number):
    from_number = os.environ["TWILIO_FROM_PHONE_NUMBER"]
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)
    client.messages.create(
                        body=notification,
                        from_=f"+{from_number}",
                        to=f"+{to_number}"
                    )


data = get_stock_data()

current_date = dt.date.today()
yesterdays_date = current_date - dt.timedelta(days=1) 
day_before_yesterdays_date = current_date - dt.timedelta(days=2)
yesterdays_market_close_time_series_key = yesterdays_date.strftime('%Y-%m-%d')
day_before_yesterdays_market_close_time_series_key = day_before_yesterdays_date.strftime('%Y-%m-%d')

try:
    yesterday_market_close_price = float(data[f"Time Series (Daily)"][yesterdays_market_close_time_series_key]["4. close"])
    day_before_yesterday_market_close_price = float(data[f"Time Series (Daily)"][day_before_yesterdays_market_close_time_series_key]["4. close"])
except KeyError:
    print("Missing data")
else:
    percentage_change = percentage_difference(day_before_yesterday_market_close_price, yesterday_market_close_price)
    if percentage_change > SENSITIVITY or percentage_change < -SENSITIVITY:
        news_data = get_news_data()
        notification_body = format_sms_notification(STOCK, percentage_change, news_data)
        if os.getenv("TWILIO_ACCOUNT_SID") != None and os.getenv("TWILIO_AUTH_TOKEN") != None and os.getenv("TWILIO_TO_PHONE_NUMBER") != None and os.getenv("TWILIO_FROM_PHONE_NUMBER") != None:
            send_sms_notification(notification_body, os.getenv("TWILIO_TO_PHONE_NUMBER"))
        else:
            print(notification_body)
