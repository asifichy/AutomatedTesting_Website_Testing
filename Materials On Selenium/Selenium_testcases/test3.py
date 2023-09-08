from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# chrome browser ------> chromedriver
# open the chrome browser
driver = webdriver.Chrome()
#Navigate to the url
driver.get("https://www.saucedemo.com/")
#Maximize the window
driver.maximize_window()

# driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
#driver.find_element(By.NAME, "password").click()
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID, "login-button").click()
time.sleep(2)
#driver.find_element(By.CSS_SELECTOR, "*[data-test=\"product_sort_container\"]").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Sauce Labs Backpack").click()
time.sleep(4)
driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
time.sleep(4)
#wait for 5 sec
time.sleep(4)
#close the window
driver.close()