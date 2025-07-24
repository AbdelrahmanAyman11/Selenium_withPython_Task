from selenium import webdriver
from selenium.webdriver.edge.service import Service
def start_driver():
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)
    service = Service("C:\\Webdriver\\msedgedriver.exe")  # تأكد إنه موجود فعليًا
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver
