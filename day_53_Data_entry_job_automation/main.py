import time
import requests
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup


# 1 create a Google form and Google table - DONE
# 2 scrap the data with the BeautifulSoup from the webpage [links], [addresses], [prices] - DONE
# 3 using selenium send it using the form that we have created - DONE

# +1 try it on the life site
# +2 could add multiple pages handler, so we could scrap data from all pages
# +3 add a possibility to change the location or parameters (user input)


load_dotenv('../.env')

SOURCE_OF_DATA = os.getenv('ZILLOW_LINK')
FORM_LINK = os.getenv('FORM_LINK')
HEADER = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept-Language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6'
}
WAIT_TIME = 10


def get_starting_data():
    response = requests.get(url=SOURCE_OF_DATA, headers=HEADER)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    all_apartments_on_page = soup.find_all(name='li', class_='ListItem-c11n-8-84-3-StyledListCardWrapper')

    all_links = []
    all_addresses = []
    all_prices = []

    for apartment in all_apartments_on_page:

        link = apartment.find_next(name='a', class_='StyledPropertyCardDataArea-anchor').get_attribute_list(key="href")
        all_links.append(link[0])

        address = apartment.find_next(name='address').getText().strip()
        all_addresses.append(address)

        price = apartment.find_next(name='span', class_='PropertyCardWrapper__StyledPriceLine').getText()
        # I need to work on a smaller solution for parsing the price
        if "+" in price:
            price = price.split('$')[1].split('+')[0]
            if "," in price:
                price = price.split(',')
                all_prices.append(f'{price[0]}{price[1]}')
            else:
                all_prices.append(price)
        else:
            price = price.split('$')[1].split('/')[0]
            if "," in price:
                price = price.split(',')
                all_prices.append(f'{price[0]}{price[1]}')
            else:
                all_prices.append(price)
    return all_addresses, all_prices, all_links


def get_driver():
    """Function returns the selenium Driver"""
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


def form_data_input_automation(driver, address_list, price_list, link_list):

    list_len_address = len(address_list)
    list_len_price = len(price_list)
    list_len_link = len(link_list)

    if list_len_address == list_len_price and list_len_price == list_len_link:
        try:
            for i in range(list_len_address + 1):

                # I have to learn how to properly use By.CSS_SELECTOR , but for now XPATH is OK
                address_field = wait_and_find_element(
                    driver,
                    By.XPATH,
                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
                )

                price_field = wait_and_find_element(
                    driver,
                    By.XPATH,
                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
                )

                link_field = wait_and_find_element(
                    driver,
                    By.XPATH,
                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
                )

                address_field.send_keys(address_list[i])
                price_field.send_keys(price_list[i])
                link_field.send_keys(link_list[i])
                submit_button = wait_and_find_element(
                    driver,
                    By.XPATH,
                    '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
                )
                submit_button.click()
                print(f"{i+1} Property has added")
                time.sleep(2)
                driver.refresh()

        except Exception as e:
            print(f'Occurred some problem in the filling the form: {e}')


def main():
    addresses, prices, links = get_starting_data()
    print('Starting data, prepared...')
    driver = get_driver()
    driver.get(FORM_LINK)
    form_data_input_automation(driver, addresses, prices, links)


if __name__ == '__main__':
    main()
    print("END")
