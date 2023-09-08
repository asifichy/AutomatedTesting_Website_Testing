from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://localhost/TheGrindCoffeeWebApplication/home.php")
time.sleep(1.5)

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
    
#to scroll up the page
i=0
while True:
    i+=1
    driver.execute_script("scrollBy(0, -400)")
    time.sleep(0.5)
    if i>15:
        break      
print("Home Page Test is Successful!") 


#about page 
about_page = driver.find_element(By.XPATH, "(//a[normalize-space()='ABOUT'])[1]")
about_page.click()
time.sleep(2)

#to scroll down the page
i=0
while True:
    i+=1
    driver.execute_script("scrollBy(0, 400)")
    time.sleep(0.5)
    if i>10:
        break 
    
#to scroll up the page
i=0
while True:
    i+=1
    driver.execute_script("scrollBy(0, -400)")
    time.sleep(0.5)
    if i>10:
        break    
print("About Page Test is Successful!") 
    
    
#product page 
product_page = driver.find_element(By.XPATH, "(//a[normalize-space()='PRODUCT'])[1]")
product_page.click()
time.sleep(2)

#to scroll down the page
i=0
while True:
    i+=1
    driver.execute_script("scrollBy(0, 400)")
    time.sleep(0.5)
    if i>10:
        break
    
#to scroll up the page
i=0
while True:
    i+=1
    driver.execute_script("scrollBy(0, -400)")
    time.sleep(0.5)
    if i>10:
        break    
print("Product Page Test is Successful!")     

#Menu page 
menu_page = driver.find_element(By.XPATH, "(//a[normalize-space()='MENU'])[1]")
menu_page.click()
time.sleep(2)

#to scroll down the page
i=0
while True:
    i+=1
    driver.execute_script("scrollBy(0, 400)")
    time.sleep(0.5)
    if i>10:
        break
    
#to scroll up the page
i=0
while True:
    i+=1
    driver.execute_script("scrollBy(0, -400)")
    time.sleep(0.5)
    if i>10:
        break    
print("Menu Page Test is Successful!") 

#Order page 
order_page = driver.find_element(By.XPATH, "(//a[normalize-space()='ORDER'])[1]")
order_page.click()
time.sleep(2)

#to scroll down the page
i=0
while True:
    i+=1
    driver.execute_script("scrollBy(0, 400)")
    time.sleep(0.5)
    if i>10:
        break    
    
#to scroll up the page
i=0
while True:
    i+=1
    driver.execute_script("scrollBy(0, -400)")
    time.sleep(0.5)
    if i>10:
        break       
print("Order Page Test is Successful!") 
    
#Contact page 
contact_page = driver.find_element(By.XPATH, "(//a[normalize-space()='CONTACT'])[1]")
contact_page.click()
time.sleep(2)

#to scroll down the page
i=0
while True:
    i+=1
    driver.execute_script("scrollBy(0, 400)")
    time.sleep(0.5)
    if i>10:
        break  
    
#to scroll down the page
i=0
while True:
    i+=1
    driver.execute_script("scrollBy(0, -400)")
    time.sleep(0.5)
    if i>10:
        break       
print("Contact Page Test is Successful!")     


#search bar
search_icon = driver.find_element(By.XPATH, "(//i[@class='fas fa-search'])[1]")
search_icon.click()
time.sleep(1.5)

test_var = ['c']
#test_var2 = ['m']

driver.find_element(By.XPATH, "(//input[@placeholder='search here...'])[1]").click()
driver.find_element(By.XPATH, "(//input[@placeholder='search here...'])[1]").send_keys(test_var)
time.sleep(1.5)

"""driver.find_element(By.XPATH, "(//input[@placeholder='search here...'])[1]").click()
driver.find_element(By.XPATH, "(//input[@placeholder='search here...'])[1]").send_keys(test_var2)"""
time.sleep(1.5)
print("Item/Product Searched Successfully!")

searchButton = driver.find_element(By.XPATH, "(//button[@name='search_btn'])[1]").click()
time.sleep(2)
print("Searching Test is Successful!\n") 

#to scroll down the page
i=0
while True:
    i+=1
    driver.execute_script("scrollBy(0, 400)")
    time.sleep(0.5)
    if i>10:
        break  
    
#to scroll down the page
i=0
while True:
    i+=1
    driver.execute_script("scrollBy(0, -400)")
    time.sleep(0.5)
    if i>10:
        break       

print("Whole Website Testing is Done Successfully!\n")

#for login
testUsername = ['asifniloy45@gmail.com']
testPassword = ['123']

def test_localhostLogin(username, password, i):
    driver.get("http://localhost/TheGrindCoffeeWebApplication/home.php")
    #time.sleep(3)
    
    driver.maximize_window()
    time.sleep(2)
    
    driver.find_element(By.XPATH, "(//div[@id='user-btn'])[1]").click() 
    time.sleep(2)
    
    driver.find_element(By.XPATH, "(//a[normalize-space()='login'])[1]").click()
    time.sleep(2)
    
    driver.find_element(By.XPATH, "(//input[@placeholder='enter your email'])[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//input[@placeholder='enter your email'])[1]").send_keys(username)
    
    driver.find_element(By.XPATH, "(//input[@placeholder='enter your password'])[1]").click()
    
    driver.find_element(By.XPATH, "(//input[@placeholder='enter your password'])[1]").send_keys(password)    
    
    driver.find_element(By.XPATH, "(//input[@name='submit'])[1]").click()
    time.sleep(2)
    
    #profile logged in state
    get_url = driver.current_url
    if(get_url == "http://localhost/TheGrindCoffeeWebApplication/home.php"):
        print("test- " + str(i) + " successfully logged in!")   
                          
    elif(get_url == "http://localhost/TheGrindCoffeeWebApplication/login.php?errcode=1"):
        print("test- " + str(i) + "failed to logged in!")     
        
    
    driver.find_element(By.XPATH, "(//div[@id='user-btn'])[1]").click()
    time.sleep(2)
    
    #profile visitng state
    driver.find_element(By.XPATH, "(//a[normalize-space()='profile'])[1]").click()
    time.sleep(1)
    print("Profile Visited Successful!")
    
    driver.find_element(By.XPATH, "(//a[normalize-space()='HOME'])[1]").click()
    time.sleep(2)    
        
    #profile logged out state        
    get_url = driver.current_url
    if(get_url == "http://localhost/TheGrindCoffeeWebApplication/home.php"):        
        driver.find_element(By.XPATH, "(//div[@id='user-btn'])[1]").click()
        driver.find_element(By.XPATH, "(//a[normalize-space()='logout'])[1]").click()
        print("test- " + str(i) + " successfully logged out!\n")    
    else:
        print("An error occurred during testing!\n")
        
lenOfList = len(testUsername)        
for i in range(0, lenOfList):
    test_localhostLogin(testUsername[i], testPassword[i], i+1)  

print("All tests are performed successsfully!\n")
    