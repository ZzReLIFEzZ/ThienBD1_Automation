
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import BaseTest, LoginPage

class Test_LoginPage(BaseTest):
    def test_login_success(self):
        login_page = LoginPage(self.driver)
        login_page.do_login("Admin", "admin123")