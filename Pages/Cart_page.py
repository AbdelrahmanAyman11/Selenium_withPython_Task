from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(3)

    def click_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
        time.sleep(2)

    def remove_first_item(self):
        try:
            remove_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Remove')]")
            time.sleep(2)

            remove_button.click()
        except Exception as e:
            print(f"Error while removing item: {e}")
