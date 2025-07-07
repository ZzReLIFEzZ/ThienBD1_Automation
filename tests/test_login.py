
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import BaseTest, LoginPage
from utils.config_reader import ConfigReader
import allure

class Test_LoginPage(BaseTest):
    @allure.story("Login thành công")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_success(self):
        login_page = LoginPage(self.driver)
        login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password())