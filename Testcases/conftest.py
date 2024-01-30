# conftest.py is a special file that is used in pytest framework
# to share fixture functions and other objects among multiple test files.
# In a hybrid framework, where pytest is used along with other frameworks or
# libraries, conftest.py can be used to share fixtures and other common configurations between the two.


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import selenium
import pytest


@pytest.fixture()
def setup():
    driver_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver







# def pytest_addoption(parser):  # This will get the value from CLI/HOOKS
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):  # This will return browser value to setup method
#     return request.config.getoption("--browser")


################pytest html report###########################
# It is hooks for adding environment info to HTML reports

# def pytest_configure(config):
#     config._metadata['project name'] = 'nop commerce'
#     config._metadata['module name'] = 'Customers'
#     config._metadata['Tester'] = 'surta'


# It is hooks for delete /modify environment info to HTML report

# @pytest.hookimpl(optionalhook=True)
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_home", None)
#     metadata.pop("plugins", None)
#     metadata['Project Name'] = 'nop commerce'
#     metadata['Module Name'] = 'Customers'
#     metadata['Tester'] = 'surta'








