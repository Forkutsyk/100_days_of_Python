import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

load_dotenv("../.env")

LINKEDIN_LOGIN = os.getenv("LINK_LOGIN")
LINKEDIN_PASSWORD = os.getenv("LINK_PASSWORD")
LINK = os.getenv("APPLICATION_LINK")
MAX_PAGES = 2
WAIT_TIME = 10

# Testing options with Claude AI
# this one is looking good

def get_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    return webdriver.Chrome(options=chrome_options)


def wait_and_find_element(driver, by, value, timeout=WAIT_TIME):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except TimeoutException:
        print(f"Element not found: {value}")
        return None


def automate_login(driver):
    try:
        sign_up_button = wait_and_find_element(
            driver,
            By.XPATH,
            '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button'
        )
        if sign_up_button:
            sign_up_button.click()

        login = wait_and_find_element(
            driver,
            By.XPATH,
            '//*[@id="base-sign-in-modal_session_key"]'
        )
        password = wait_and_find_element(
            driver,
            By.XPATH,
            '//*[@id="base-sign-in-modal_session_password"]'
        )

        if login and password:
            login.send_keys(LINKEDIN_LOGIN)
            password.send_keys(LINKEDIN_PASSWORD, Keys.ENTER)
            time.sleep(2)
        return True
    except Exception as e:
        print(f"Login error: {e}")
        return False


def close_chat(driver):
    try:
        chat_buttons = driver.find_elements(By.CSS_SELECTOR, "button.msg-overlay-bubble-header__button")
        if chat_buttons:
            chat_buttons[0].click()
            time.sleep(1)
    except Exception as e:
        print(f"Error closing chat: {e}")


def add_to_watchlist(driver):
    try:
        follow_button = wait_and_find_element(
            driver,
            By.CSS_SELECTOR,
            "button.jobs-save-button"
        )
        if follow_button:
            follow_button.click()
            time.sleep(1)
            return True
    except Exception as e:
        print(f"Error adding to watchlist: {e}")
    return False


def go_to_next_page(driver):
    try:
        next_button = wait_and_find_element(
            driver,
            By.CSS_SELECTOR,
            "button.artdeco-pagination__button--next"
        )
        if next_button and next_button.is_enabled():
            next_button.click()
            time.sleep(2)
            return True
    except Exception as e:
        print(f"Error going to next page: {e}")
    return False


def process_job_listings(driver):
    page_count = 0

    while page_count < MAX_PAGES:
        try:
            job_cards = driver.find_elements(
                By.CSS_SELECTOR,
                ".job-card-container--clickable"
            )

            if not job_cards:
                print("No job listings found")
                break

            for job in job_cards:
                try:
                    job.click()
                    time.sleep(2)

                    position = job.find_element(
                        By.CSS_SELECTOR,
                        ".job-card-list__title--link"
                    )
                    company = job.find_element(
                        By.CSS_SELECTOR,
                        ".artdeco-entity-lockup__subtitle"
                    )

                    print(f'Position: {position.get_attribute("aria-label")}')
                    print(f'Company: {company.text}')

                    if add_to_watchlist(driver):
                        print("Added to watchlist")

                    driver.execute_script(
                        'arguments[0].scrollIntoView({ behavior: "smooth", block: "start" });',
                        job
                    )
                    time.sleep(1)

                except Exception as e:
                    print(f"Error processing job: {e}")
                    continue

            page_count += 1
            if page_count < MAX_PAGES and not go_to_next_page(driver):
                break

        except Exception as e:
            print(f"Error processing page: {e}")
            break


def main():
    driver = get_driver()
    try:
        driver.get(LINK)
        print("Starting the bot...")
        time.sleep(2)

        if not automate_login(driver):
            print("Login failed")
            return

        close_chat(driver)
        process_job_listings(driver)

    except Exception as e:
        print(f"Main error: {e}")
    finally:
        driver.quit()
        print("Bot finished")


if __name__ == '__main__':
    main()
