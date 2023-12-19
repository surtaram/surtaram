from selenium.webdriver.common.by import By


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    first_name_xpath = "//input[@name='firstname']"
    last_name_xpath = "//input[@name='lastname']"
    email_xpath = "//input[@name='email']"
    telephone_xpath = "//input[@name='telephone']"
    password_xpath = "//input[@name='password']"
    confirm_password_xpath = "//input[@name='confirm']"
    privacy_policy_checkbox_xpath = "//input[@type='checkbox']"
    continue_button_xpath = "//input[@value='Continue']"

    warning_message_privacy_policy_xpath = "//*[@id='account-register']/div[1]"
    warning_message_pwd_confirm_not_same_xpath = "//*[@id='content']/form/fieldset[2]/div[2]/div/div"
    warning_message_duplicate_email_id_xpath = "//*[@id='account-register']/div[1]"

    def enter_first_name(self, first_name):
        self.driver.find_element(By.XPATH, self.first_name_xpath).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.XPATH, self.last_name_xpath).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def enter_telephone(self, telephone):
        self.driver.find_element(By.XPATH, self.telephone_xpath).send_keys(telephone)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys(confirm_password)

    def click_on_privacy_policy_checkbox(self):
        self.driver.find_element(By.XPATH, self.privacy_policy_checkbox_xpath).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

    def warning_message_privacy_policy_checkbox(self, expected_message):
        return self.driver.find_element(By.XPATH, self.warning_message_privacy_policy_xpath).text. \
            __eq__(expected_message)

    def password_n_confirm_password_not_same(self, expected_message):
        return self.driver.find_element(By.XPATH, self.warning_message_pwd_confirm_not_same_xpath).text. \
            __eq__(expected_message)

    def duplicate_email_warning_message(self, expected_message):
        return self.driver.find_element(By.XPATH, self.warning_message_duplicate_email_id_xpath).text. \
            __eq__(expected_message)


