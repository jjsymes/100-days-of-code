from selenium import webdriver
from selenium.webdriver.common.by import By
import subprocess


URL="https://www.python.org/"


chrome_driver_path = "/usr/local/bin/chromedriver"
chrome_driver_path = subprocess.check_output(["which", "chromedriver"])
chrome_driver_path = chrome_driver_path.strip()
driver = webdriver.Chrome(chrome_driver_path)

driver.get(URL)
event_widget = driver.find_element(By.CLASS_NAME, "event-widget")
event_elements = event_widget.find_elements(By.TAG_NAME, "li")

events = {}

for index, event_element in enumerate(event_elements):
    time = event_element.find_element(By.TAG_NAME, "time").get_attribute("datetime")
    events.update({
        index: {
            "time": time[0:10],
            "name": event_element.find_element(By.TAG_NAME, "a").text
        }
    })

print(events)

driver.quit()