  #-------------------------- Selenium preparation ------------------------
  
#pip install selenium 

#-------------------------- Chrome preparation --------------------------
# ensure that current chrome version is installed in the default directory 
# webdrivers location https://chromedriver.chromium.org/


#-------------------------- Necessary imports ---------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# chrome browser ------> chromedriver
# open the chrome browser

# Specify the path to the ChromeDriver executable
service = Service(executable_path="F:\Selenium drivers and jar files\Chrome driver\chromedriver.exe")

# Configure Chrome options
options = webdriver.ChromeOptions()

# Create a WebDriver instance
driver = webdriver.Chrome(service=service, options=options)
#Navigate to the url
driver.get("https://www.google.com/")
time.sleep(3)
#Maximize the window
driver.maximize_window()
time.sleep(3)
kichu = driver.find_elements(By.TAG_NAME, "a")
print(len(kichu))
time.sleep(3)
print("Success")
#wait for 3 sec
time.sleep(3)
#close the window
driver.close()












#search_box = driver.find_element(By.NAME, "q")
#search_box.send_keys("Selenium with Python")
#search_box.submit()
#search_results = driver.find_elements(By.CLASS_NAME, "g")
#for result in search_results:
# #   print(result.text)