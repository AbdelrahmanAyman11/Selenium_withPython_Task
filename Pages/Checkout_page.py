from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
    error_message_locator = (By.CSS_SELECTOR, "h3[data-test='error']")  

    def click_continue_without_info(self):
        self.driver.find_element(By.ID, "continue").click()

    def get_error_message(self):
        return self.driver.find_element(By.CLASS_NAME, "error-message-container").text
   
    def fill_checkout_info(self):
        self.driver.find_element(By.ID, "first-name").send_keys("first")
        self.driver.find_element(By.ID, "last-name").send_keys("last")
        self.driver.find_element(By.ID, "postal-code").send_keys("11111")
   
    def click_finish(self):
        self.driver.find_element(By.ID, "finish").click()

    def get_thank_you_message(self):
        return self.driver.find_element(By.CLASS_NAME, "complete-header").text


