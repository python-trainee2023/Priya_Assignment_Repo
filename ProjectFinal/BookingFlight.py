from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


from ProjectFinal.BaseTest import BaseTest
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestFlight(BaseTest):

    def test_checkFlight(self):

        cross_botton = self.driver.find_element(By.XPATH, "//div[@class='vvTc-item-button']")
        cross_botton.click()
        time.sleep(3)


        departureCity = self.driver.find_element(By.XPATH, "//input[@aria-label='Flight origin input']")
        departureCity.send_keys("AHEMDABAD GUJRAT")
        time.sleep(2)
        departureCity.send_keys(Keys.RETURN)


        destinationCity = self.driver.find_element(By.XPATH, "//input[@aria-label='Flight destination input']")
        destinationCity.send_keys("NEW DELHI")
        time.sleep(3)
        destinationCity.send_keys(Keys.RETURN)


        ways = self.driver.find_element(By.XPATH, "//div[@aria-label='Trip type Return']")
        ways.click()
        time.sleep(2)
        waysOption = self.driver.find_element(By.XPATH, "//span[text()='One-way']")
        waysOption.click()
        time.sleep(3)


        personCategory = self.driver.find_element(By.XPATH, "//div[@class='S9tW S9tW-pres-default']")
        personCategory.click()
        time.sleep(2)
        add_person = self.driver.find_element(By.XPATH, "//input[@aria-label='Children']")
        add_person.click()
        time.sleep(2)
        person_increment = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div[1]/div[4]/div/button[2]")
        person_increment.click()
        time.sleep(3)

        # action_click = ActionChains(driver)
        # action_click.move_to_element(add_person).move_to_element(person_increment.click().perform()

        chooseDate = self.driver.find_element(By.XPATH, "//span[@aria-live='polite']")
        chooseDate.click()
        time.sleep(2)
        fixDate = self.driver.find_element(By.XPATH, "//div[@aria-label='Friday 20 October, 2023']")
        fixDate.click()
        time.sleep(3)

        findFlightDeals = self.driver.find_element(By.XPATH, "//div[@class='zEiP-formField zEiP-submit']")
        findFlightDeals.click()
        time.sleep(30)

