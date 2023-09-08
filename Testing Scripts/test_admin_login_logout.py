from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

testUsername = ['admin']
testPassword = ['111']

def test_localhostAdminLogin(username, password, i):
    driver.get("http://localhost/TheGrindCoffeeWebApplication/home.php")
    #time.sleep(3)
    driver.maximize_window()  
    time.sleep(1.5) 
    
    driver.get("http://localhost/TheGrindCoffeeWebApplication/admin/admin_login.php")
    time.sleep(2)
    

    
    # Finding the input fields and submit button
    username_input = driver.find_element(By.XPATH, "(//input[@name='name'])[1]")
    password_input = driver.find_element(By.XPATH, "(//input[@name='pass'])[1]")
    time.sleep(2)
    
    # Input test data
    username_input.send_keys(username)  
    password_input.send_keys(password)

    #click on login button
    loginBtn = driver.find_element(By.XPATH, "(//input[@name='submit'])[1]")
    loginBtn.click() 

    time.sleep(3)
           
        
    get_url = driver.current_url
    if(get_url == "http://localhost/TheGrindCoffeeWebApplication/admin/dashboard.php"):
        print("test- " + str(i) + " successfully logged in into Admin Panel!")
        
        driver.find_element(By.XPATH, "(//span[normalize-space()='Sign Out'])[1]").click()
        print("test- " + str(i) + " successfully logged out from Admin Panel!\n") 
               
    elif(get_url == "http://localhost/TheGrindCoffeeWebApplication/login.php?errcode=1"):
        print("test- " + str(i) + " failed to logged in into Admin Panel!\n")   
        
    else:
        print("An error occurred during testing!\n")
        
lenOfList = len(testUsername)        
for i in range(0, lenOfList):
    test_localhostAdminLogin(testUsername[i], testPassword[i], i+1)    
    