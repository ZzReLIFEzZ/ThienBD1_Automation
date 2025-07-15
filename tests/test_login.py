from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import BaseTest, LoginPage
from utils.config_reader import ConfigReader
from selenium.webdriver.support.ui import WebDriverWait
import allure

class Test_LoginPage(BaseTest):
    # @allure.story("Login thành công")
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_login_success(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password())
    #     # Kiểm tra xem đã đăng nhập thành công chưa
    #     dashboard_header = self.driver.find_element(By.TAG_NAME, "h6").text
    #     assert dashboard_header == "Dashboard", "Login failed - Dashboard not found"

    @allure.story("Test chụp hình allure khi element không có")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_allure_failed(self):  # driver là fixture WebDriver
        login_page = LoginPage(self.driver)
        try:
            login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password1())
            error_locator = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")
            error_element = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(error_locator)
            )
            assert "Invalid abc" in error_element.text, "Expected text not found"
        except Exception as e:
            with allure.step("Capture screenshot on failure"):
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    name="Screenshot_on_Failure",
                    attachment_type=allure.attachment_type.PNG
                )
            raise e