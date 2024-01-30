import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Teacher:
    Enter_attendance_link_text = " Enter Attendance"
    Enter_marks_link_text = "Enter Marks"
    View_Timetable_link_text = 'View TimeTable'
    Generate_reports_link_text = "Generate Reports"
    teacher_home_page_link_text = 'Welcome Trisila'

    def __init__(self, driver):
        self.driver = driver

    def Click_on_enter_attendance(self):
        self.driver.find_element(By.LINK_TEXT, self.Enter_attendance_link_text).click()

    def Click_on_enter_marks(self):
        self.driver.find_element(By.LINK_TEXT, self.Enter_marks_link_text).click()

    def Click_on_View_timetable(self):
        self.driver.find_element(By.LINK_TEXT, self.View_Timetable_link_text).click()

    def Click_on_generate_reports(self):
        self.driver.find_element(By.LINK_TEXT, self.Generate_reports_link_text).click()

    def Verify_H1_heading(self):
        h1 = self.driver.find_element(By.LINK_TEXT, self.teacher_home_page_link_text).text
        return h1
