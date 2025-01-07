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


def processing_the_offer(driver):
    # while True:
    try:
        ul_element = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/ul')
        li_elements = ul_element.find_elements(By.TAG_NAME, "li")

        print(len(li_elements))
        print(type(li_elements))
        for i in li_elements:
            print(i.text)
        # for element in list_items:
        #     element.click()
        #     time.sleep(2)
        #     position = element.find_element(By.CSS_SELECTOR, value=".job-card-list__title--link")
        #     company_name = element.find_element(By.CSS_SELECTOR, value=".artdeco-entity-lockup__subtitle")
        #     driver.execute_script('arguments[0].scrollIntoView({ behavior: "smooth", block: "start" });', element)
        #
        #     print(f'Position: {position.get_attribute("aria-label")}')
        #     print(f'Company: {company_name.text}\n')
        #     # try:
        #     #     driver.find_element(By.CSS_SELECTOR, "button.artdeco-pagination__button--next")
        #     #     break
        #     # except Exception as e:
        #     #     print(f"There a no next page button{e}")
        #
        # print(type(list_items))
        # list_items = []
        # print(len(list_items))
    except Exception as e:
        print(f"There are some troble in the processin the offer: {e}")


def main():
    driver = get_driver()
    driver.get(LINK)
    print("Starting doing some stuff...")
    time.sleep(2)
    automate_login(driver)
    chat_buttons = driver.find_elements(By.CSS_SELECTOR, "button.msg-overlay-bubble-header__button")
    if chat_buttons:
        chat_buttons[0].click()
        time.sleep(1)
    processing_the_offer(driver)

    driver.quit()


if __name__ == '__main__':
    main()
    print("END")
