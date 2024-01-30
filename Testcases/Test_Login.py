# here we can write test case and this is first test case.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
from Pages.Adminpage import Login
# import requests
from utilities.Custome_Loggers import LogGen
from utilities.ReadProperties import Readconfig


class Test_001_Login:
    baseURL = Readconfig.getapplicationurl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("*************Test_001_Login*******************")
        self.logger.info("***********verifying home page title***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        # self.driver.close()
        if act_title == "Login":
            assert True
            self.driver.close()
            self.logger.info("*************Home page title test case passed**************")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*************Home page title test case failed***************")
            assert False

    def test_login(self, setup):
        self.logger.info("****************verifying login test*****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.Enter_Username(self.username)
        self.lp.Enter_password(self.password)
        self.lp.click_login_button()
        act_title = self.driver.title
        # self.driver.close()
        if act_title == "homepage":
            assert True
            self.logger.info("***************Login test case passed****************")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_login.png")
            self.driver.close()
            self.logger.info("***************Login test case failed******************")
            assert False
