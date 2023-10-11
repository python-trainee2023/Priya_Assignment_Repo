import time
from selenium import webdriver

class BaseTest:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.in.cheapflights.com/")
        time.sleep(3)



    def teardown(self):
        self.driver.quit()