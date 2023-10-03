from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


class BaseTest:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demoblaze.com")

    def teardown(self):
        self.driver.quit()


class SignUpDemo(BaseTest):
    @pytest.mark.parametrize("user_name", ["userpriya"])
    def test_signup(self, user_name):
        self.driver.find_element(By.ID, "signin2").click()
        username = self.driver.find_element(By.ID, "sign-username")
        username.send_keys(user_name)
        time.sleep(10)
        password = self.driver.find_element(By.ID, "sign-password")
        password.send_keys("priya123")
        time.sleep(10)
        self.driver.find_element(By.CLASS_NAME, "btn btn-primary").click()
        time.sleep(15)
        print("successfully Signed Up!!!")