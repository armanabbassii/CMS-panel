from Locators import *


class Login:

    def __int__(self, driver):
        self.driver = driver

    def login_with_username(self):
        self.driver.find_element('xpath', username_button_class).click()
