from selenium import webdriver

global driver
driver = webdriver.Chrome()


def get_driver():

    return driver