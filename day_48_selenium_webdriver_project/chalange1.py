from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')

item_list = {}
dates = driver.find_elements(By.CSS_SELECTOR, value='.event-widget ul li time')
events = driver.find_elements(By.CSS_SELECTOR, value='.menu ul li a')

for element in range(len(dates)):
    item_list[element] = {
        'time': dates[element].text,
        'event name': events[element].text
    }
    print(item_list)
# driver.close()
driver.quit()
