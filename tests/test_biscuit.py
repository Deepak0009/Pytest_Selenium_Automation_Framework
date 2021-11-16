import pytest
from pageObjects import page_home, page_biscuit


@pytest.mark.usefixtures("onetimeSetup")
class TestBiscuitPurchase:

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.home = page_home.Home(self.driver)
        self.biscuit = page_biscuit.Biscuit(self.driver)

    def test_purchase(self):
        self.home.locationSelect()
        self.home.searchBiscuit()
        self.home.clickSearch()
        self.biscuit.selectBiscuit()
