import pytest
from selenium import webdriver

from utilities import Readconfigurations
from utilities.Readconfigurations import read_configuration


@pytest.fixture()
def setup_and_teardown(request):
    browser = Readconfigurations.read_configuration("basic info", "browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    else:
        print("provide valid browser name")
    driver.maximize_window()
    website_url = Readconfigurations.read_configuration("basic info", "url")
    print(website_url)
    driver.get(website_url)
    request.cls.driver = driver
    yield
    driver.quit()
