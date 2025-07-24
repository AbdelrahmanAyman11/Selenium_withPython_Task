import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.driver_setup import start_driver

@pytest.fixture(scope="module")
def driver():
    driver = start_driver()
    yield driver
    driver.quit()
