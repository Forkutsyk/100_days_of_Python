import time
import requests
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


# 1 create a Google form and Google table - DONE
# 2 scrap the data with the BeautifulSoup from the webpage [links], [addresses], [prices] - DONE
# 3 using selenium send it using the form that we have created

load_dotenv('../.env')

SOURCE_OF_DATA = os.getenv('LINK')
HEADER = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept-Language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6'
}


def get_starting_data():
    response = requests.get(url=SOURCE_OF_DATA, headers=HEADER)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    all_properties_on_page = soup.find_all(name='li', class_='ListItem-c11n-8-84-3-StyledListCardWrapper')

    all_links = []
    all_addresses = []
    all_prices = []

    for property in all_properties_on_page:
        link = property.find_next(name='a', class_='StyledPropertyCardDataArea-anchor').get_attribute_list(key="href")
        all_links.append(link[0])
        address = property.find_next(name='address').getText().strip()
        all_addresses.append(address)
        price = property.find_next(name='span', class_='PropertyCardWrapper__StyledPriceLine').getText()
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
    # print(all_links)
    # print(len(all_links))
    #
    # print(all_prices)
    # print(len(all_prices))
    #
    # print(all_addresses)
    # print(len(all_addresses))

if __name__ == '__main__':
    get_starting_data()
    print("END")