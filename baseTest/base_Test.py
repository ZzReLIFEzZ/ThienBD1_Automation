import pytest
from selenium import webdriver

class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print(f"\nThe Web's title is : {self.driver.title}")
        request.cls.driver = self.driver
        yield
        self.driver.quit()