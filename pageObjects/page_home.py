from webdriverObejcts.base import Base
from selenium.webdriver.common.keys import Keys


class Home(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def locationSelect(self):
        element = self.driver.find_element_by_xpath("//input[@placeholder='Type your city Society/Colony/Area']")
        weblement = element.send_keys('Pune, Maharashtra, India')
        weblement.send_keys(Keys.ENTER)

    def searchBiscuit(self):
        self.driver.find_element_by_xpath("//input[@class='react-autosuggest__input']")

    def clickSearch(self):
        self.driver.find_element_by_xpath("//button[@class='btn search__btn']").click()