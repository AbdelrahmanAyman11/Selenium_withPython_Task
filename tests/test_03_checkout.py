import pytest
from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.Cart_page import CartPage
from Pages.Checkout_page import CheckoutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_checkout_without_customer_info(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_first_product_to_cart()

    cart = CartPage(driver)
    cart.go_to_cart()
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.click_continue_without_info()

    error_msg = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(checkout.error_message_locator)
    ).text

    assert "Error" in error_msg, "Expected error when continuing without customer info."


def test_checkout_with_empty_cart(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    cart = CartPage(driver)
    cart.go_to_cart()
    cart.remove_first_item()
    cart.click_checkout()

    ch= CheckoutPage(driver)

    ch.fill_checkout_info()
    ch.click_continue_without_info()
    ch.click_finish()
    thank_you_text = ch.get_thank_you_message()
    assert "THANK YOU FOR YOUR ORDER" in thank_you_text.upper()
