import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from baseTest.base_Test import BaseTest

import time

class Test_LoginPage(BaseTest):
    def test_login_success(self):
        # Chờ tối đa 100 giây để phần tử xuất hiện
        username = WebDriverWait(self.driver, 100).until(
        EC.presence_of_element_located((By.NAME, "username"))
        )
        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")
        if(username):
            username.send_keys("Admin")
            password.send_keys("admin123")
        else:
            print("KHONG TIM THAY USERNAME")

        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        time.sleep(10)