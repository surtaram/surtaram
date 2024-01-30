import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Teacher_details:
    Home_xpath = "//*[@id='wrapper']/ul/li[1]/a"
    Attendance_xpath = '//*[@id="wrapper"]/ul/li[2]/a'
    Marks_xpath = '//*[@id="wrapper"]/ul/li[3]/a'
    Time_table_xpath = '//*[@id="wrapper"]/ul/li[4]/a'
    Reports_xpath = '//*[@id="wrapper"]/ul/li[5]/a'

    def __init__(self, driver):
        self.driver = driver

    def Click_On_Home(self):
        self.driver.find_element(By.XPATH, self.Home_xpath).click()

    def Click_On_Attendance(self):
        self.driver.find_element(By.XPATH, self.Attendance_xpath).click()

    def Click_On_Marks(self):
        self.driver.find_element(By.XPATH, self.Marks_xpath).click()

    def Click_On_Time_Table(self):
        self.driver.find_element(By.XPATH, self.Time_table_xpath).click()

    def Click_On_Reports(self):
        self.driver.find_element(By.XPATH, self.Reports_xpath).click()
