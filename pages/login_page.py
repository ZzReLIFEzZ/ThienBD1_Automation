from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tests.base_test import BaseTest
from pages.base_page import BasePage
import time

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # Call the constructor of BasePage
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")


    def do_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        time.sleep(10)
    
    def enter_username(self, username):
        username_element = self.wait_element(self.username_field)
        username_element.send_keys(username)

    def enter_password(self, password):
        password_element = self.wait_element(self.password_field)
        password_element.send_keys(password)

    def click_login_button(self):
        self.click(self.login_button)