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
toggle_numbers = driver.find_element(By.ID, "toggleNumbers")
toggle_flash = driver.find_element(By.ID, "toggleFlash")
toggle_numbers.click()
toggle_flash.click()

last_bought_item = "buyCursor"
buy_items = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab", "buyPortal", "buyTime machine"]

while True:
    try:
        cookie.click()
        buy_available_item = driver.find_elements(By.CSS_SELECTOR, "#store div[class='']")[-1]
        available_item_id = buy_available_item.get_attribute("id")
        if available_item_id in buy_items:
            if last_bought_item != available_item_id:
                buy_items.remove(last_bought_item)
            buy_available_item.click()
            last_bought_item = available_item_id
    except:
        pass

driver.quit()
