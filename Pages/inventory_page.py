from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_first_product_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    
    def get_first_product_add_button(self):
      try:
        wait = WebDriverWait(self.driver, 10)
        # استنى أول زر Add to cart أو Remove يظهر
        add_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn_inventory")))
        return add_button
      except:
        return None