from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_signin_field(self):
        signInField = self.driver.find_element(By.XPATH, "//a[@id ='nav-link-accountList']")
        signInField.click()
        sleep(2)

    def fill_username_field(self, username):
        userNameFieldElement = self.driver.find_element(By.ID, "ap_email")
        userNameFieldElement.clear()
        userNameFieldElement.send_keys(username)
        sleep(3)

    def click_continue_button(self):
        continueButtonElement = self.driver.find_element(By.ID, "continue")
        continueButtonElement.click()
        sleep(3)

    def fill_password_field(self, password):
        passwordFieldElement = self.driver.find_element(By.ID, "ap_password")
        passwordFieldElement.send_keys(password)
        sleep(7)

    def click_signin_button(self):
        signInButtonElement = self.driver.find_element(By.ID, "signInSubmit")
        signInButtonElement.click()
        sleep(3)

