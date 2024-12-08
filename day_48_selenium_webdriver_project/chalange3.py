from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=chrome_options)
driver.get('https://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.NAME, value='fName')
last_name = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')
first_name.send_keys('Python')
last_name.send_keys('Python2')
email.send_keys('email.@email.com', Keys.ENTER)

