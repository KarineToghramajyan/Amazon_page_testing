import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
time.sleep(2)

userNameFieldElement = driver.find_element(By.ID, "ap_email")
userNameFieldElement.clear()
userNameFieldElement.send_keys("testamazon117@gmail.com")

continueButtonElement = driver.find_element(By.ID, "continue")
continueButtonElement.click()
time.sleep(3)

passwordFieldElement = driver.find_element(By.ID, "ap_password")
passwordFieldElement.send_keys("molotok123")
time.sleep(7)

signInButtonElement = driver.find_element(By.ID, "signInSubmit")
signInButtonElement.click()
time.sleep(5)

driver.close()