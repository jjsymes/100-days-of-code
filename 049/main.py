from selenium import webdriver
from selenium.webdriver.common.by import By
import subprocess
import os
from time import sleep


URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=software%20developer&location=London%2C%20England%2C%20United%20Kingdom"
APPLY_ENABLED = False
SAVE_ENABLED = True

LINKEDIN_USERNAME = os.environ["LINKEDIN_USERNAME"]
LINKEDIN_PASSWORD = os.environ["LINKEDIN_PASSWORD"]
PHONE_NUMBER = os.environ["PHONE_NUMBER"]

chrome_driver_path = subprocess.check_output(["which", "chromedriver"]).strip()
driver = webdriver.Chrome(chrome_driver_path)

driver.get(URL)
sleep(2)

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys(LINKEDIN_USERNAME)
password.send_keys(LINKEDIN_PASSWORD)
submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()

apply_urls = []

sleep(3)

job_posts = driver.find_elements(By.CLASS_NAME, "job-card-container")

for index in range(3):
    job_posts[index].click()
    sleep(2)
    if SAVE_ENABLED:
        save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        save_button.click()
    if APPLY_ENABLED:
        # Not tested
        apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
        apply_button.click()
        sleep(1)
        form = driver.find_element(By.CLASS_NAME, "jobs-easy-apply-content")
        phone_entry = form.find_element(By.CLASS_NAME, "fb-single-line-text").find_element(By.TAG_NAME, "input")
        phone_entry.send_keys(PHONE_NUMBER)
        next = form.find_element(By.TAG_NAME, "button")
        next.click()

driver.quit()
