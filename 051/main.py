import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import subprocess
from time import sleep


SPEEDTEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/login"

PROMISED_UP = 10
PROMISED_DOWN = 64

TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]

class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.promised_up = PROMISED_UP
        self.promised_down = PROMISED_DOWN
        self.up = 0
        self.down = 0
        chrome_driver_path = subprocess.check_output(["which", "chromedriver"]).strip()
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.implicitly_wait(60)

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)
        accept = self.driver.find_element(By.ID, "_evidon-banner-acceptbutton")
        accept.click()
        button = self.driver.find_element(By.CSS_SELECTOR, ".js-start-test.test-mode-multi")
        button.click()
        self.up = float(self.driver.find_element(By.CSS_SELECTOR, ".result-data-large.number.result-data-value.download-speed").text)
        self.down = float(self.driver.find_element(By.CSS_SELECTOR, ".result-data-large.number.result-data-value.upload-speed").text)

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        user_input = self.driver.find_element(By.NAME, "text")
        sleep(1)
        user_input.click()
        sleep(1)
        user_input.send_keys(TWITTER_EMAIL)
        sleep(1)
        user_input.send_keys(Keys.ENTER)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        tweet_input = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
        tweet_input.click()
        tweet_input.send_keys(f"Hey internet provider, why is my internet speed is {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up")
        send_tweet = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span")
        send_tweet.click()

    def quit(self):
        self.driver.quit()

internet_speed_twitter_bot = InternetSpeedTwitterBot()
internet_speed_twitter_bot.get_internet_speed()
internet_speed_twitter_bot.tweet_at_provider()
internet_speed_twitter_bot.quit()
