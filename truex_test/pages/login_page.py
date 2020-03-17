from truex_test.locators.login import *
from truex_test.settings import USER_LOGIN, USER_PASSWORD


class LoginPage:

    def login_into_truex_interface(self):
        self.driver.find_element(*email_input).send_keys(USER_LOGIN)
        self.driver.find_element(*password_input).send_keys(USER_PASSWORD)
        self.driver.find_element(*submit_button).click()
