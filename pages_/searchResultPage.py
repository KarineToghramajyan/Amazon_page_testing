from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchResults():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_first_result(self):
        firstResult = self.driver.find_element(By.XPATH, "//*[@data-image-index='1']")
        sleep(2)
        firstResult.click()
        sleep(5)