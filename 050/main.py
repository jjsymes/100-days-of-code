from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import subprocess
from time import sleep


URL = "https://tinder.com/"

# Will swipe either left or right
SWIPE_RIGHT = True

chrome_driver_path = subprocess.check_output(["which", "chromedriver"]).strip()
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(120)

driver.get(URL)

# Must manually sign in due to 2 Factor Auth
sign_in_button = driver.find_element(By.CSS_SELECTOR, "a.button")
sign_in_button.click()

#Allow location
allow_location_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

#Disallow notifications
notifications_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Allow cookies
cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

driver.implicitly_wait(2)

for _ in range(100):
    sleep(1)

    try:
        if SWIPE_RIGHT:
            swipe_left_button = driver.find_element(By.XPATH, "//*[@id=\"u-1510067323\"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[4]/div/div[2]/button")
            swipe_right_button.click()
        else:
            swipe_right_button = driver.find_element(By.XPATH, "//*[@id=\"u-1510067323\"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[4]/div/div[4]/button")
            swipe_left_button.click()
    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()
