import pytest
from selenium.webdriver.common.by import By
from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.Cart_page import CartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module", autouse=True)
def login_once(driver):
    """Login once for all tests in this module"""
    LoginPage(driver).login("standard_user", "secret_sauce")
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

def test_add_and_remove_item(driver):
    """Verify that a product can be added to the cart and then removed"""
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    inventory.add_first_product_to_cart()

    badge = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert badge.text == "1", "Cart badge did not update after adding item"

    cart.go_to_cart()
    cart.remove_first_item()

    WebDriverWait(driver, 5).until_not(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
    )
    assert len(driver.find_elements(By.CLASS_NAME, "cart_item")) == 0, "Item still present after removal"

def test_cannot_increase_quantity_of_same_item(driver):
    """Verify that user cannot increase quantity of the same product in cart"""
    print("\n🚀 Running test_cannot_increase_quantity_of_same_item")
    driver.get("https://www.saucedemo.com/inventory.html") 
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    # Add first product
    inventory.add_first_product_to_cart()

    # Try to locate the add button again (should be replaced by "Remove")
    add_button = inventory.get_first_product_add_button()
    assert "Remove" in add_button.text or not add_button.is_enabled(), "User can re-add same product"

    # Go to cart
    cart.go_to_cart()

    # Verify only one item in the cart
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 1, "Duplicate item added to cart"

    # Verify quantity is displayed and not editable
    quantity_element = driver.find_element(By.CLASS_NAME, "cart_quantity")
    assert quantity_element.text == "1", "Quantity is not 1"
    assert quantity_element.tag_name != "input", "Quantity should not be editable input field"
