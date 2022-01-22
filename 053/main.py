from http import HTTPStatus
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import subprocess
from time import sleep

FORM_URL = "https://forms.gle/yBFrp6sXkpvMnc4VA"
ZILLOW_LISTINGS_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

def get_properties_from_page(html):
    soup = BeautifulSoup(html, "html.parser")

    property_cards = soup.find_all(name="article", class_="list-card")

    properties = []

    for card in property_cards:
        link = card.find(class_="list-card-link")
        if link:
            link = link.get("href")
        else:
            continue
        pcm = card.find(class_="list-card-price")
        if pcm:
            pcm = pcm.get_text().rstrip("/mo")
        else:
            continue
        address = card.find(class_="list-card-addr")
        if address:
            address = address.get_text()
        else:
            continue
        property = {
            "address": address,
            "pcm": pcm,
            "link": link,
        }
        properties.append(property)
    
    return properties


def get_properties(listings_url):
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }

    response = requests.get(listings_url, headers=header)

    html = response.text
    cookie = response.cookies

    print("Getting properties from page 1.")
    properties = get_properties_from_page(html)

    more_properties = True
    next_page = 2
    while more_properties == True:
        next_page_url = f"https://www.zillow.com/homes/for_rent/1-_beds/{next_page}_p/"
        response = requests.get(next_page_url, headers=header, cookies=cookie)
        if response.status_code == HTTPStatus.OK:
            html = response.text
            cookie = response.cookies
            print(f"Getting properties from page {next_page}.")
            properties.extend(get_properties_from_page(html))
            next_page += 1
        else:
            print("No more properties.")
            more_properties = False

    # remove duplicates
    properties_pruned = []
    [properties_pruned.append(property) for property in properties if property not in properties_pruned]

    return properties_pruned

def automate_data_entry(google_form_url, properties):
    chrome_driver_path = subprocess.check_output(["which", "chromedriver"]).strip()
    driver = webdriver.Chrome(chrome_driver_path)
    driver.implicitly_wait(60)

    for property in properties:
        driver.get(google_form_url)
        sleep(4)
        inputs = driver.find_elements(By.CSS_SELECTOR, "input[type=text]")
        address_input = inputs[0]
        price_input = inputs[1]
        link_input = inputs[2]
        address_input.send_keys(property["address"])
        price_input.send_keys(property["pcm"])
        link_input.send_keys(property["link"])
        submit = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
        submit.click()

    driver.quit()

properties = get_properties(ZILLOW_LISTINGS_URL)

automate_data_entry(FORM_URL, properties)