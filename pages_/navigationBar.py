from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class NavigationBar():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def fill_search_box(self):
        searchFieldElement = self.driver.find_element(By.ID, "twotabsearchtextbox")
        searchFieldElement.click()
        searchFieldElement.send_keys("iphone charger")

    def click_search_icon(self):
        searchIconElement = self.driver.find_element(By. ID, "nav-search-submit-button")
        searchIconElement.click()

    def click_cart_button(self):
        cartButtonElement = self.driver.find_element(By.ID, "nav - cart - text - container")
        cartButtonElement.click()







