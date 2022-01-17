from selenium import webdriver
from selenium.webdriver.common.by import By
import subprocess


url="https://en.wikipedia.org/wiki/Main_Page"


chrome_driver_path = "/usr/local/bin/chromedriver"
chrome_driver_path = subprocess.check_output(["which", "chromedriver"])
chrome_driver_path = chrome_driver_path.strip()
driver = webdriver.Chrome(chrome_driver_path)

driver.get(url)
article_count_element = driver.find_element(By.ID, "articlecount")
article_count = article_count_element.find_element(By.TAG_NAME, "a").text

print(article_count)

url="https://en.wikipedia.org/wiki/Main_Page"

driver.get("http://secure-retreat-92358.herokuapp.com/")
form_first_name = driver.find_element(By.NAME, "fName")
form_last_name = driver.find_element(By.NAME, "lName")
form_email = driver.find_element(By.NAME, "email")
sign_up_button = driver.find_element(By.CSS_SELECTOR, "form button")

form_first_name.send_keys("Joe")
form_last_name.send_keys("Bloggs")
form_email.send_keys("joebloggs@example.com")
sign_up_button.click()

driver.quit()
