from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.AccountPage import AccountPage
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    email_address_xpath = "//input[@name='email']"
    password_xpath = "//input[@name='password']"
    login_button_xpath = "//input[@class='btn btn-primary']"
    warning_message_xpath="//div[@id='account-login']/div[1]"

    def enter_email_address(self, email_add):
        self.type_into_element(email_add,"email_address_xpath",self.email_address_xpath)
        # self.driver.find_element(By.XPATH, self.email_address_xpath).send_keys(email_add)

    def enter_password(self, password):
        self.type_into_element(password,"password_xpath",self.password_xpath)
        # self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def click_on_login_button(self):
        self.click_on_element("login_button_xpath",self.login_button_xpath)
        # self.driver.find_element(By.XPATH,self.login_button_xpath).click()
        return AccountPage(self.driver)

    def retrieve_warning_message(self,expected_message):
        return self.driver.find_element(By.XPATH,self.warning_message_xpath).text.__contains__(expected_message)


