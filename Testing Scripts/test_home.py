from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://localhost/TheGrindCoffeeWebApplication/home.php")
time.sleep(1)

driver.maximize_window()  
time.sleep(2)


#to scroll down the page
i=0
while True:
    i+=1
    driver.execute_script("scrollBy(0, 400)")
    time.sleep(0.5)
    if i>15:
        break
 
#to scroll down the page
i=0
while True:
    i+=1
    driver.execute_script("scrollBy(0, -400)")
    time.sleep(0.5)
    if i>15:
        break
    
    
