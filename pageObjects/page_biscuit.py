from webdriverObejcts.base import Base


class Biscuit(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def selectBiscuit(self):
        self.driver.find_element_by_xpath()