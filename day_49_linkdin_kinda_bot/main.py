import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

load_dotenv("../.env")

LINKEDIN_LOGIN = os.getenv("LINK_LOGIN")
LINKEDIN_PASSWORD = os.getenv("LINK_PASSWORD")
LINK = os.getenv("APPLICATION_LINK")
MINIMUM = 5


def get_driver():
    """Function returns the selenium Driver"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    return webdriver.Chrome(options=chrome_options)


def automate_login(driver):
    """
    Function automatically logging in the system.
    Input: Selenium driver
    Output: None
    """
    sign_up_button = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
    sign_up_button.click()
    login = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_key"]')
    password = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_password"]')
    time.sleep(2)
    login.send_keys(LINKEDIN_LOGIN)
    password.send_keys(LINKEDIN_PASSWORD, Keys.ENTER)


def main():
    driver = get_driver()
    driver.get(LINK)
    print("Starting doing nasty stuff...")
    time.sleep(2)
    automate_login(driver)


if __name__ == '__main__':
    main()
    print("END")
