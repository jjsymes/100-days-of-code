from selenium import webdriver
from selenium.webdriver.common.by import By
import subprocess


URL="http://orteil.dashnet.org/experiments/cookie/"


chrome_driver_path = "/usr/local/bin/chromedriver"
chrome_driver_path = subprocess.check_output(["which", "chromedriver"])
chrome_driver_path = chrome_driver_path.strip()
driver = webdriver.Chrome(chrome_driver_path)

driver.get(URL)

cookie = driver.find_element(By.ID, "cookie")
buy_cursor = driver.find_element(By.ID, "buyCursor")
buy_grandma = driver.find_element(By.ID, "buyGrandma")
buy_factory = driver.find_element(By.ID, "buyFactory")
buy_mine = driver.find_element(By.ID, "buyMine")
buy_shipment = driver.find_element(By.ID, "buyShipment")
buy_alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
buy_portal = driver.find_element(By.ID, "buyPortal")
buy_time_machine = driver.find_element(By.ID, "buyTime machine")

while True:
    try:
        cookie.click()
        buy_available_item = driver.find_element(By.CSS_SELECTOR, "#store div[class='']")
        buy_available_item.click()
    except:
        pass

driver.quit()
