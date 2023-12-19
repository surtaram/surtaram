from datetime import datetime
import pytest
from selenium.webdriver.common.by import By

from Pages.AccountPage import AccountPage
from Pages.HomePage import Homepage
from Pages.RegisterPage import RegisterPage
from tests.Basetest import BaseTest


class Test_register(BaseTest):
    def test_register_with_mandatory_field(self):
        home_page = Homepage(self.driver)
        home_page.click_on_my_account()
        register_page=home_page.select_register_option()
        register_page.enter_first_name('Ram')
        register_page.enter_last_name("kumar")
        email_id = self.generate_email_with_time_stamp()
        register_page.enter_email(email_id)
        register_page.enter_telephone("7837994390")
        register_page.enter_password("ram@kumar")
        register_page.enter_confirm_password("ram@kumar")
        register_page.click_on_privacy_policy_checkbox()
        register_page.click_on_continue_button()
        account_page = AccountPage(self.driver)
        expected_text = "Your Account Has Been Created!"
        assert account_page.account_successfully_created_message(expected_text)

    def test_register_without_clicking_on_privacy(self):
        home_page = Homepage(self.driver)
        home_page.click_on_my_account()
        register_page=home_page.select_register_option()

        register_page.enter_first_name('Ram')
        register_page.enter_last_name("kumar")
        email_id = self.generate_email_with_time_stamp()
        register_page.enter_email(email_id)
        register_page.enter_telephone("7837994390")
        register_page.enter_password("ram@kumar")
        register_page.enter_confirm_password("ram@kumar")

        register_page.click_on_continue_button()
        expected_text = "Warning: You must agree to the Privacy Policy!"
        assert register_page.warning_message_privacy_policy_checkbox(expected_text)

    def test_register_with_psw_with_mismatch_confirm_pwd(self):
        home_page = Homepage(self.driver)
        home_page.click_on_my_account()
        register_page=home_page.select_register_option()
        register_page.enter_first_name('Ram')
        register_page.enter_last_name("kumar")
        email_id = self.generate_email_with_time_stamp()
        register_page.enter_email(email_id)
        register_page.enter_telephone("7837994390")
        register_page.enter_password("ram@kumar")
        register_page.enter_confirm_password("ram@kumar123")
        register_page.click_on_privacy_policy_checkbox()
        register_page.click_on_continue_button()
        expected_text = "Password confirmation does not match password!"

        assert register_page.password_n_confirm_password_not_same(expected_text)

    def test_register_with_duplicate_email_add(self):
        home_page = Homepage(self.driver)
        home_page.click_on_my_account()
        register_page=home_page.select_register_option()
        register_page.enter_first_name('Ram')
        register_page.enter_last_name("kumar")
        register_page.enter_email("test@gmail.com")
        register_page.enter_telephone("7837994390")
        register_page.enter_password("ram@kumar")
        register_page.enter_confirm_password("ram@kumar")
        register_page.click_on_privacy_policy_checkbox()
        register_page.click_on_continue_button()
        expected_text = "Warning: E-Mail Address is already registered!"

        assert register_page.duplicate_email_warning_message(expected_text)

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y%md%H%M%S")
        email = "test" + time_stamp + "@gmail.com"
        print(email)
        return email
