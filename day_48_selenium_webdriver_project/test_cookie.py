import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

## The best on my old laptop wih not really god internet is 41,8cps
# I could also try mozilla driver (it seems to be faster)

class CookieBot:
    def __init__(self):
        self.bought_upgrades = 0
        with open("testing_results.json", 'r') as stats_data:
            print('Open stats file...')
            self.stats = json.load(stats_data)
        self.main_logic()

    def initialize_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        return webdriver.Chrome(options=chrome_options)

    def stats_results(self, driver, start_time):
        result = driver.find_element(By.ID, value="cps").text
        money = driver.find_element(By.ID, value='money').text
        stats = {
            "time": time.time() - start_time,
            "cookies/sec": float(result.split(':')[1]),
            "Cookies at the end": int(money),
            "Upgrades bought": self.bought_upgrades
        }
        self.stats.append(stats)
        with open("testing_results.json", 'w') as data:
            print('Writing down the results...')
            json.dump(self.stats, data, indent=4)

    def get_store_prices(self, driver):
        print("checking the ids...")
        store_items_ids = []
        store_items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
        for item in store_items:
            try:
                store_items_ids.insert(0, item.get_attribute("id"))
                # print("added")

            except Exception as e:
                print(f"Could not interact with item: {e}")
        print('\nList created')
        return store_items_ids

    def main_logic(self):
        driver = self.initialize_driver()
        driver.get('https://orteil.dashnet.org/experiments/cookie/')
        print('driver initialized !')

        big_cookie = driver.find_element(By.ID, 'cookie')
        store = self.get_store_prices(driver)

        start_time = time.time()
        end_time = (5 * 60) + start_time
        last_action_time = time.time()

        print("started clicking")
        while not time.time() >= end_time:
            for click in range(15):
                big_cookie.click()
            if (time.time() - last_action_time) >= 15: # 15 / 10 bad

                for item in range(len(store)):
                    try:
                        # just trying to buy upgrade from the most expensive to less
                        # PS:checking the price with every iteration will slow down the Bot even more
                        store_item = driver.find_element(By.ID, f'{store[item]}')
                        store_item.click()


                    except Exception as e:
                        # XD just trying to max out efficiency of this bot
                        # print(f"Occurred some error in the buying upgrade part:{e}")
                        pass
                last_action_time = time.time()
                self.bought_upgrades += 1
                print('upgrade bought')

        self.stats_results(driver, start_time)


if __name__ == "__main__":
    cookie = CookieBot()
    print("The End")
