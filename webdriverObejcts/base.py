from selenium import webdriver


class Base:
    def __init__(self, driver):
        self.driver = driver

    def verigyTitle(self):
        assert self.driver.title
