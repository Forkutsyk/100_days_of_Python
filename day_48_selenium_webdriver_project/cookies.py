# 1009 for 5 minutes only clicking
# 8,7 per second in first try
# 12,8 per seconds second try (18/11) // added if statement + changed from 5 to 10 sec

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/cookieclicker/')
stats = {}
bought_upgrades = 0
# Handle the cookie consent
try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.fc-button.fc-cta-consent.fc-primary-button'))
    ).click()
    print("Consent button clicked.")
except Exception as e:
    print(f"Could not find or click the consent button: {e}")

# Select English language
try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'langSelect-EN'))
    ).click()
    print("Language set to English.")
except Exception as e:
    print(f"Could not find or click the language button: {e}")

# Start the game
try:
    cookie_button = driver.find_element(By.ID, 'bigCookie')
    start_time = time.time()
    duration = 5 * 60
    last_action_time = time.time()

    while time.time() - start_time < duration:
        cookie_button.click()
        if (time.time() - last_action_time) >= 10:
            # print(time.time() - start_time)
            # print("looking for the upgrade\n")

            cookie_button.click()
            try:
                products_available = driver.find_elements(By.CSS_SELECTOR, value='.product.unlocked.enabled')
                last_action_time = time.time()
                if len(products_available) > 0:
                    products_available[len(products_available) - 1].click()
                    bought_upgrades += 1
                else:
                    print("No upgrade available")
            except Exception as e:
                print(f"Occurred some error in the clicking cookie part: {e}\n")
    result = driver.find_element(By.ID, value="cookiesPerSecond").text.split()

    print("Finished clicking.")
    print(f"cookies/second: {result[2]}")
    print(f"Upgrades bought:{bought_upgrades}")
    stats = {
        "time": time.time() - start_time,
        "cookies/sec": result[2],
        "Upgrades bought": bought_upgrades
    }

except Exception as e:
    print(f"Could not find or click the cookie button: {e}")

with open("testing results.json", 'w') as data:
    json.dump(stats, data, indent=4)
