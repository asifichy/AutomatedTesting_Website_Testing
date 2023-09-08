from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

testUsername = ['admin']
testPassword = ['111']

def test_localhostAdminLogin(username, password, i):
    driver.get("http://localhost/TheGrindCoffeeWebApplication/home.php")
    time.sleep(2)
    
    driver.get("http://localhost/TheGrindCoffeeWebApplication/admin/admin_login.php")
    time.sleep(1)
    
    driver.maximize_window()  
    time.sleep(3) 
    
    # Finding the input fields and submit button
    username_input = driver.find_element(By.XPATH, "(//input[@name='name'])[1]")
    password_input = driver.find_element(By.XPATH, "(//input[@name='pass'])[1]")
    time.sleep(2)
    
    # Input test data
    username_input.send_keys(username)  
    password_input.send_keys(password)

    #click on login/submit button
    loginBtn = driver.find_element(By.XPATH, "(//input[@name='submit'])[1]")
    loginBtn.click() 

    #time.sleep(2)
    
    #testing admin panel
    #product page
    test_product = driver.find_element(By.XPATH, "(//a[@href='products.php'])[1]")
    test_product.click()
    time.sleep(2)
    
    test_dashboard = driver.find_element(By.XPATH, "(//a[@class='logo'])[1]")
    test_dashboard.click()
    time.sleep(2)
    
    #placed order page
    test_placed_order = driver.find_element(By.XPATH, "(//a[@href='placed_orders.php'])[1]")
    test_placed_order.click()
    time.sleep(2)
    
    test_dashboard = driver.find_element(By.XPATH, "(//a[@class='logo'])[1]")
    test_dashboard.click()
    time.sleep(2)
    
    #admin page
    test_admin_panel = driver.find_element(By.XPATH, "(//a[@href='admin_accounts.php'])[1]")
    test_admin_panel.click()
    time.sleep(2)
    
    test_dashboard = driver.find_element(By.XPATH, "(//a[@class='logo'])[1]")
    test_dashboard.click()
    time.sleep(2)
    
    #employee page
    test_employee_panel = driver.find_element(By.XPATH, "(//a[@href='employee_accounts.php'])[1]")
    test_employee_panel.click()
    time.sleep(2)
    
    test_dashboard = driver.find_element(By.XPATH, "(//a[@class='logo'])[1]")
    test_dashboard.click()
    time.sleep(2)
    
    #user page
    test_user = driver.find_element(By.XPATH, "(//a[@href='users_accounts.php'])[1]")
    test_user.click()
    time.sleep(2)
    
    test_dashboard = driver.find_element(By.XPATH, "(//a[@class='logo'])[1]")
    test_dashboard.click()
    time.sleep(2)
    
    #message page
    test_message = driver.find_element(By.XPATH, "(//a[@href='messages.php'])[1]")
    test_message.click()
    time.sleep(2)
    
    test_dashboard = driver.find_element(By.XPATH, "(//a[@class='logo'])[1]")
    test_dashboard.click()
    time.sleep(2)
    
    #product page
    test_dashboard = driver.find_element(By.XPATH, "(//a[@class='logo'])[1]")
    test_dashboard.click()
    time.sleep(2)
    
        
    get_url = driver.current_url
    if(get_url == "http://localhost/TheGrindCoffeeWebApplication/admin/dashboard.php"):
        print("test- " + str(i) + " successfully logged in into Admin Panel!\nTested all the Admin Pages.\n")
        
        driver.find_element(By.XPATH, "(//span[normalize-space()='Sign Out'])[1]").click()
        print("test- " + str(i) + " successfully logged out from Admin Panel!\n and operation compelte!\n") 
               
    elif(get_url == "http://localhost/TheGrindCoffeeWebApplication/login.php?errcode=1"):
        print("test- " + str(i) + " failed to logged in into Admin Panel!\n")   
        
    else:
        print("An error occurred during signup testing!\n")
        
lenOfList = len(testUsername)        
for i in range(0, lenOfList):
    test_localhostAdminLogin(testUsername[i], testPassword[i], i+1)    
    