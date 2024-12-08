from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/cookieclicker/')

while True:
    i = 0
    consents_lint = driver.find_element(By.LINK_TEXT, value='Consent')
    consents_lint.click()
    language_link = driver.find_element(By.LINK_TEXT, value='English')
    language_link.click()
    while i != 5:
        cookie_button = driver.find_element(By.CSS_SELECTOR, value='#bigCookie')
        cookie_button.click()

        i += 0

    available_items = driver.find_elements(By.CSS_SELECTOR, value='.product unlocked enabled')
    for item in range(len(available_items)):
        item_product = driver.find_element(By.CSS_SELECTOR, value=f'#productPrice{item}')
        print(item_product.text)

    break