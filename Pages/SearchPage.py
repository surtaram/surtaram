from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__int__(driver)
        # self.driver = driver

    search_result_Link_text = "HP LP3065"
    invalid_search_result_xpath = "//input[@type='button']//following-sibling::p"

    def display_status_of_valid_product(self):
        return self.check_display_status_of_element("search_result_Link_text",self.search_result_Link_text)
        # return self.driver.find_element(By.LINK_TEXT, self.search_result_Link_text).is_displayed()

    def invalid_search_result_warning_msg_xpath(self, expected_message):
        # return self.retrieve_element_text(self.invalid_search_result_xpath)
        return self.driver.find_element(By.XPATH, self.invalid_search_result_xpath).text.__eq__(expected_message)
