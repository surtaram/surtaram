from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

from utilities import ExcelUtilities
from Pages.AccountPage import AccountPage
from Pages.HomePage import Homepage
from Pages.LoginPage import LoginPage
from tests.Basetest import BaseTest


class Test_login(BaseTest):
    @pytest.mark.parametrize("email_address,password",
                             ExcelUtilities.get_data_from_excel("Excelfiles/data_driven.xlsx", "Sheet1"))
    def test_login_with_valid_credentials(self, email_address, password):
        home_page = Homepage(self.driver)
        home_page.click_on_my_account()
        login_page = home_page.select_login()
        login_page.enter_email_address(email_address)
        login_page.enter_password(password)
        account_page = login_page.click_on_login_button()
        try:
            assert account_page.display_status_of_edit_ur_acc_info_option()
        except:
            expected_warning_message = 'Warning: No match for E-Mail Address and/or Password.'
            assert login_page.retrieve_warning_message(expected_warning_message)

    def test_login_with_invalid_email_valid_password(self):
        home_page = Homepage(self.driver)
        home_page.click_on_my_account()
        login_page = home_page.select_login()
        invalid_email = self.generate_email_with_time_stamp()
        login_page.enter_email_address(invalid_email)
        login_page.enter_password("123456")
        login_page.click_on_login_button()
        expected_warning_message = 'Warning: No match for E-Mail Address and/or Password.'
        assert login_page.retrieve_warning_message(expected_warning_message)

    def test_login_valid_email_add_invalid_password(self):
        home_page = Homepage(self.driver)
        home_page.click_on_my_account()
        login_page = home_page.select_login()
        login_page.enter_email_address("demotest@gmail.com")
        login_page.enter_password("123431231")
        login_page.click_on_login_button()
        expected_warning_message = 'Warning: No match for E-Mail Address and/or Password.'
        assert login_page.retrieve_warning_message(expected_warning_message)

    def test_login_without_entering_credentials(self):
        home_page = Homepage(self.driver)
        home_page.click_on_my_account()
        login_page = home_page.select_login()
        login_page.enter_email_address(" ")
        login_page.enter_password(" ")
        login_page.click_on_login_button()
        expected_warning_message = 'Warning: No match for E-Mail Address and/or Password.'
        assert login_page.retrieve_warning_message(expected_warning_message)
