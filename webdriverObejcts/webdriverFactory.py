from selenium import webdriver
import time


class webdriverFunction:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def webdriverObject(self):
        if self.driver == "Firefox":
            self.driver = webdriver.Firefox
        elif self.driver == "Edge":
            self.driver = webdriver.Edge
        else:
            self.driver = webdriver.Chrome('E:/chromedriver/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(20)
        return self.driver
