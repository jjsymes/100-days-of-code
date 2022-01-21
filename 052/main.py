import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import subprocess
from time import sleep


TARGET_ACCOUNT = "stealthnottingham"
INSTAGRAM_URL = "https://www.instagram.com"

USERNAME = os.environ["INSTAGRAM_USERNAME"]
PASSWORD = os.environ["PASSWORD"]

class InstaFollower:
    def __init__(self) -> None:
        chrome_driver_path = subprocess.check_output(["which", "chromedriver"]).strip()
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.implicitly_wait(60)

    def login(self):
        self.driver.get(f"{INSTAGRAM_URL}/accounts/login/")
        accept = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]")
        accept.click()
        sleep(3)
        user = self.driver.find_element(By.NAME, "username")
        user.click()
        user.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, "password")
        password.click()
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(3)

    def find_followers(self):
        self.driver.get(f"{INSTAGRAM_URL}/{TARGET_ACCOUNT}")
        sleep(3)
        list_followers = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        list_followers.click()
        sleep(2)

    def follow(self):
        buttons = self.driver.find_elements(By.XPATH, "//button[text()=\"Follow\"]")
        for button in buttons:
            button.click()

    def quit(self):
        self.driver.quit()

internet_speed_twitter_bot = InstaFollower()
internet_speed_twitter_bot.login()
internet_speed_twitter_bot.find_followers()
internet_speed_twitter_bot.follow()
internet_speed_twitter_bot.quit()
