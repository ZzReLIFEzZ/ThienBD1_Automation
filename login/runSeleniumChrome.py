import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

class BaseTest:
    @pytest.fixture(scope="class", autouse=True)

    def setup(self, request):
        # Use Service object instead of deprecated 'executable_path'
        self.driver = webdriver.Chrome()
        
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print(f"\nThe Web's title is : {self.driver.title}")
        
        request.cls.driver = self.driver
        yield
        self.driver.quit()

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