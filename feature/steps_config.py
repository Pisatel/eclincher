from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

global driver
driver = webdriver.Chrome()
#driver = webdriver.Firefox()


def get_driver():
    driver.maximize_window()
    return driver
