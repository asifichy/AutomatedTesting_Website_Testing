from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# chrome browser ------> chromedriver
# open the chrome browser
driver = webdriver.Chrome()
#Navigate to the url
driver.get("https:\\demo.applitools.com")
#Maximize the window
driver.maximize_window()

# driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys("Admin")
time.sleep(3)
#driver.find_element(By.NAME, "password").click()
driver.find_element(By.ID, "password").send_keys("admin")
time.sleep(3)
driver.find_element(By.ID, "log-in").click()
#wait for 5 sec
time.sleep(3)
#close the window
driver.close()