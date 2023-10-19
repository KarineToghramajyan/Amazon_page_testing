from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class CartPage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_cart_button(self):
        cartButtonElement = self.driver.find_element(By.ID, "nav - cart - text - container")
        cartButtonElement.click()

    def add_to_cart(self):
        addToCartButton = self.driver.find_element(By.ID, "add-to-cart-button")
        addToCartButton.click()
        sleep(3)

    def go_to_cart(self):
        goToCartButton = self.driver.find_element(By.XPATH, "//*[@data-csa-c-content-id='sw-gtc_CONTENT']")
        goToCartButton.click()
        sleep(2)

    def decrease_item_quantity(self):
        quantityButton = self.driver.find_element(By.ID, "a-autoid-0-announce")
        quantityButton.click()
        deleteItemOption = self.driver.find_element(By.ID, "quantity_0")
        deleteItemOption.click()
        sleep(3)