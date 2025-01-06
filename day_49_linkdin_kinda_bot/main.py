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

# I don't want to apply for every "easy apply" job available, want to change a little the ending functionality.
# also have a problem if I run the bot too often (2 times in 5 min), LinkedIn keep redirecting me to the another screen of logging

# Probably just use this project to practice with selenium XD


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


# Should I keep this 1 line def XD
def get_all_list_items(driver):
    """
    Function to get all elements from the job list.
    Input: Selenium driver
    Output: List of WebElement objects
    """

    return driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")


def main():
    driver = get_driver()
    driver.get(LINK)
    print("Starting doing some stuff...")
    time.sleep(2)
    automate_login(driver)

    list_items = get_all_list_items(driver)
    print(len(list_items))
    for element in list_items:
        # don't know if this script is working correctly// need to test it
        driver.execute_script('arguments[0].scrollIntoView({ behavior: "smooth", block: "start" });', element)
        time.sleep(2)
        element.click()
        time.sleep(2)
        position = element.find_element(By.CSS_SELECTOR, value=".job-card-list__title--link")
        company_name = element.find_element(By.CSS_SELECTOR, value=".artdeco-entity-lockup__subtitle")
        print(f'Position: {position.get_attribute("aria-label")}')
        print(f'Company: {company_name.text}\n')
    driver.quit()


if __name__ == '__main__':
    main()
    print("END")
