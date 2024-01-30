import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Login:
    username_xpath = "//input[@name='username']"
    password_xpath = "//input[@name='password']"
    Login_button_xpath = "//button[@type='submit']"
    Logout_button_link_text="Logout"

    def __init__(self, driver):
        self.driver = driver

    def Enter_Username(self,username):
        self.driver.find_element(By.XPATH,self.username_xpath).send_keys(username)

    def Enter_password(self,password):
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH,self.Login_button_xpath).click()

    def click_Logout_button(self):
        self.driver.find_element(By.LINK_TEXT,self.Logout_button_link_text).click()

    




