from Locators import *


class SSOLogin:

    def __init__(self, driver):
        self.driver = driver

    def sso_username(self, username):
        self.driver.find_element('xpath', username_textbox_name).send_keys(sso_username)

    def sso_password(self, password):
        self.driver.find_element('xpath', password_textbox_name).send_keys(sso_password)