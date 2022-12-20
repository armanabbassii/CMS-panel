from Locators import *


class SSOLogin:
#??? def and __init
    def __init__(self, driver):
        self.driver = driver

    def sso_username(self, username):
        self.driver.find_element('xpath', username_textbox_name).send_keys(username)

    def sso_password(self, password):
        self.driver.find_element('xpath', password_textbox_name).send_keys(password)

    def sso_go(self):
        self.driver.find_element('xpath', go_button_name).click()

    def sso_users(self):
        self.driver.find_element('xpath', users_button_title).click()