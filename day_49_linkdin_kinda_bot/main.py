import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv("../.env")

LINKEDIN_LOGIN = os.getenv("LINK_LOGIN")
LINKEDIN_PASSWORD = os.getenv("LINK_PASSWORD")
LINK = os.getenv("APPLICATION_LINK")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(LINK)

if __name__ == '__main__':
    sign_up_button = driver.find_element(By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
    print("Doin stuff...")
    sign_up_button.click()
    login = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_key"]')
    password = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_password"]')
    login.send_keys(LINKEDIN_LOGIN)
    password.send_keys(LINKEDIN_PASSWORD, Keys.ENTER)

# ## just testing the login functionality
# still need to working around a "Application functionallity"  i think in my case just the "Save" functionallity