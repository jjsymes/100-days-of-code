import requests
from bs4 import BeautifulSoup
import smtplib
import os


PRODUCT_URL="https://www.amazon.co.uk/AMD-Ryzen-5950X-Processor-Cache/dp/B0815Y8J9N/ref=sr_1_1?crid=1S8YP0MRN002L&keywords=amd+5950x&qid=1642302588&sprefix=amd+5950x%2Caps%2C72&sr=8-1"
TARGET_PRICE=660.00
EMAIL_NOTIFICATION_TO=os.getenv("EMAIL_NOTIFICATION_TO")
EMAIL_NOTIFICATION_FROM=os.getenv("EMAIL_NOTIFICATION_FROM")
EMAIL_NOTIFICATION_FROM_PASSWORD=os.getenv("EMAIL_NOTIFICATION_FROM_PASSWORD")


def notify(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL_NOTIFICATION_FROM, password=EMAIL_NOTIFICATION_FROM_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_NOTIFICATION_FROM,
            to_addrs=EMAIL_NOTIFICATION_TO,
            msg=f"Subject:Price Alert\n\n{message}".encode('utf-8')
        )


def get_product_price(product_url):
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }

    html = requests.get(product_url, headers=header).text
    soup = BeautifulSoup(html, "html.parser")
    price_whole_html_element = soup.find(name="span", class_="a-price-whole")
    price_decimal_html_element = soup.find(name="span", class_="a-price-fraction")
    price = float(price_whole_html_element.contents[0]) + float(price_decimal_html_element.contents[0])
    return price


price = get_product_price(PRODUCT_URL)

if price <= TARGET_PRICE:
    message = f"Product price (£{price}) lower than target price (£{TARGET_PRICE}). Link: {PRODUCT_URL}"
    print(message)
    if EMAIL_NOTIFICATION_TO and EMAIL_NOTIFICATION_FROM and EMAIL_NOTIFICATION_FROM_PASSWORD:
        notify(message)
else:
    print(f"Product price (£{price}) is not lower than target price (£{TARGET_PRICE}).")
