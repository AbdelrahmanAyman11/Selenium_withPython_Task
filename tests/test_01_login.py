import pytest
from selenium.webdriver.common.by import By
from Pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_setup import start_driver
def test_valid_login(driver):
    """User can log in with correct credentials"""
    LoginPage(driver).login("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory")
    )

    assert "inventory" in driver.current_url, "User was not redirected to inventory page"

@pytest.mark.parametrize(
    "username,password",
    [
        ("invalid_user", "secret_sauce"),
        ("standard_user", "wrong_password"),
        ("", "secret_sauce"),
        ("standard_user", ""),
    ],
)
def test_invalid_login(driver, username, password):
    """
    Login should fail with incorrect data and display an error banner
    """
    LoginPage(driver).login(username, password)

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )

    assert error.is_displayed(), "Error message not shown for invalid login"
