from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tests.base_test import BaseTest
import time

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def do_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        time.sleep(5)
    
    def enter_username(self, username):
        username_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_field)
        )
        username_element.send_keys(username)

    def enter_password(self, password):
        password_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_field)
        )
        password_element.send_keys(password)

    def click_login_button(self):
        login_button_element = self.driver.find_element(*self.login_button)
        login_button_element.click()