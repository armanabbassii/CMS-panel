from Pages.Login import Login
from Pages.SSOLogin import SSOLogin
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import unittest


##??
class LoginTests(unittest.TestCase):
    ##??
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        cls.driver.implicitly_wait(3)

    ##???
    def valid_login_vs_SSOLogin_tests(self):
        self.driver.get('http://dev.cms.test/')
        login = Login(driver=self.driver)
        ssologin = SSOLogin(driver=self.driver)
        login.login_with_username()
        ssologin.sso_username('omid1')
        ssologin.sso_password('m@123456')
        ssologin.sso_go()
        ssologin.sso_users()
        sleep(5)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()

    if __name__ == '__main__':
        unittest.main()