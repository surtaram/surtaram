import pytest
from selenium.webdriver.common.by import By

from Pages.HomePage import Homepage
from Pages.SearchPage import SearchPage
from tests.Basetest import BaseTest


class Test_search(BaseTest):

    def test_search_for_a_valid_product(self):
        home_page = Homepage(self.driver)
        search_page = home_page.search_for_a_product("HP")
        assert search_page.display_status_of_valid_product()

    def test_search_for_a_invalid_product(self):
        home_page = Homepage(self.driver)
        search_page = home_page.search_for_a_product("HONDA")
        expected_text = 'There is no product that matches the search criteria.'
        assert search_page.invalid_search_result_warning_msg_xpath(expected_text)
