import pytest
import json
from webdriverObejcts.webdriverFactory import webdriverFunction


@pytest.fixture(scope='session')
def config():
    readFile = open(r'C:/Users/ABC/PycharmProjects/Grofers/testData/testData.json')
    return json.load(readFile)


@pytest.fixture(scope='class')
def onetimeSetup(request, config):
    wdf = webdriverFunction(config["browser"], config["url"])
    driver = wdf.webdriverObject()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()