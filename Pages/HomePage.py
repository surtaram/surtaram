from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.RegisterPage import RegisterPage
from Pages.SearchPage import SearchPage


class Homepage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    search_box_field_xpath = "//input[@name='search']"
    search_button_xpath = "//button[@class='btn btn-default btn-lg']"
    my_account_drop_menu_xpath = "//i[@class='fa fa-user']//following-sibling::span[1]"
    select_Login_from_drop_down_Link_text = "Login"
    select_Register_from_drop_down_Link_text = "Register"

    def enter_product_into_search_box_field(self, value):
        self.type_into_element(value, "search_box_field_xpath", self.search_box_field_xpath, )
        # self.driver.find_element(By.XPATH, self.search_box_field_xpath).send_keys(value)

    def click_on_search_box_button(self):
        self.click_on_element("search_button_xpath", self.search_button_xpath)
        # self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        return SearchPage(self.driver)

    def click_on_my_account(self):
        self.click_on_element("my_account_drop_menu_xpath", self.my_account_drop_menu_xpath)

        # self.driver.find_element(By.XPATH, self.my_account_drop_menu_xpath).click()

    def select_login(self):
        self.click_on_element("select_Login_from_drop_down_Link_text", self.select_Login_from_drop_down_Link_text)
        # self.driver.find_element(By.LINK_TEXT, self.select_Login_from_drop_down_Link_text).click()
        return LoginPage(self.driver)

    def select_register_option(self):
        self.click_on_element("select_Register_from_drop_down_Link_text", self.select_Register_from_drop_down_Link_text)

        # self.driver.find_element(By.LINK_TEXT, self.select_Register_from_drop_down_link_text).click()
        return RegisterPage(self.driver)

    def search_for_a_product(self, product_name):
        self.enter_product_into_search_box_field(product_name)
        self.click_on_search_box_button()
        return SearchPage(self.driver)

    def navigate_to_login_page(self):
        self.click_on_my_account()
        self.select_login()
        return LoginPage(self.driver)
