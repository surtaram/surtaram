from selenium.webdriver.common.by import By


class AccountPage:

    def __init__(self, driver):
        self.driver = driver

    edit_ur_acc_info_option_link_text = "Edit your account information"
    account_successfully_created_warning_message_xpath = "//div[@id='content']/h1"

    def display_status_of_edit_ur_acc_info_option(self):
        return self.driver.find_element(By.LINK_TEXT, self.edit_ur_acc_info_option_link_text).is_displayed()

    def account_successfully_created_message(self, expected_message):
        return self.driver.find_element(By.XPATH, self.account_successfully_created_warning_message_xpath).text.__eq__(
            expected_message)


