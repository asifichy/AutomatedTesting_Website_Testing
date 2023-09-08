from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

#Home page visit and scroll down and up
driver.get("http://localhost/TheGrindCoffeeWebApplication/home.php")
time.sleep(1)

driver.maximize_window()  
time.sleep(3)

"""#to scroll down the page
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
        break"""
    

testUsername = ['asifniloy45@gmail.com']
testPassword = ['123']

#for login test
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
    
    """#profile visitng state
    driver.find_element(By.XPATH, "(//a[normalize-space()='profile'])[1]").click()
    time.sleep(1)
    print("Profile Visit is Successful!")"""
    
    driver.find_element(By.XPATH, "(//a[normalize-space()='HOME'])[1]").click()
    time.sleep(2)  
    
    
    #go to product page
    driver.find_element(By.XPATH, "(//a[normalize-space()='PRODUCT'])[1]").click() #ok till this part 
    time.sleep(2)  

    """#to scroll down the page
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
            break"""                    
     
    #add product into cart  
    driver.find_element(By.XPATH, "(//div[@class='heading'])[1]")
    driver.find_element(By.XPATH, "(//h3[normalize-space()='our menu'])[1]")
    driver.find_element(By.XPATH, "(//p)[2]") 
    driver.find_element(By.XPATH, "(//section[@class='products'])[1]")
    driver.find_element(By.XPATH, "(//h1[normalize-space()='Coffee to Boost Your Day'])[1]")
    driver.find_element(By.XPATH, "(//div[@class='box-container'])[1]")
    driver.find_element(By.XPATH, "(//img)[2]")
    time.sleep(2)
    
    add_to_cart_button = driver.find_element(By.XPATH, "(//button[@name='add_to_cart'])[1]")
    action = ActionChains(driver)
    action.move_to_element(add_to_cart_button).perform()
    time.sleep(2)
    
    add_to_cart_button.click()
    time.sleep(2)
    
    """quick_view= driver.find_element(By.XPATH, "(//a[@class='fas fa-eye'])[1]")
    action = ActionChains(driver)
    action.move_to_element(quick_view).perform()
    time.sleep(2)
    
    quick_view.click()
    time.sleep(2)"""    
    

    #show message
    print(driver.find_element(By.XPATH, "(//div[@class='message'])[1]"))

    #cart icon 
    driver.find_element(By.XPATH, "(//i[@class='fas fa-shopping-cart'])[1]").click()
    time.sleep(2)              
    
    #view product and towards checkout  
    driver.find_element(By.XPATH, "(//div[@class='heading'])[1]")  
    driver.find_element(By.XPATH, "(//h3[normalize-space()='shopping cart'])[1]")
    driver.find_element(By.XPATH, "(//p)[2]") 
    driver.find_element(By.XPATH, "(//section[@class='products'])[1]")
    driver.find_element(By.XPATH, "(//h1[normalize-space()='your cart'])[1]")
    driver.find_element(By.XPATH, "(//div[@class='box-container'])[1]")
    driver.find_element(By.XPATH, "(//div[@class='cart-total'])[1]")
    driver.find_element(By.XPATH, "(//a[normalize-space()='proceed to checkout'])[1]")
    time.sleep(2)   
    
    #to scroll down the page
    i=0
    while True:
        i+=1
        driver.execute_script("scrollBy(0, 400)")
        time.sleep(0.5)
        if i>5:
            break
     
    
    #checkout page
    driver.find_element(By.XPATH, "(//div[@class='heading'])[1]")  
    driver.find_element(By.XPATH, "(//h3[normalize-space()='checkout'])[1]")
    driver.find_element(By.XPATH, "(//p)[2]") 
    driver.find_element(By.XPATH, "(//section[@class='checkout'])[1]")
    driver.find_element(By.XPATH, "(//h1[normalize-space()='order summary'])[1]")
    driver.find_element(By.XPATH, "(//div[@class='box-container'])[1]")
    driver.find_element(By.XPATH, "(//div[@class='cart-total'])[1]")
    driver.find_element(By.XPATH, "(//a[normalize-space()='proceed to checkout'])[1]")
    driver.find_element(By.XPATH, "(//input[@name='submit'])[1]")
    time.sleep(2)        
    
    #show message
    print(driver.find_element(By.XPATH, "(//div[@class='message'])[1]"))
    
    #go to order page
    driver.find_element(By.XPATH, "(//a[normalize-space()='ORDER'])[1]")
    
    #to scroll down the page
    i=0
    while True:
        i+=1
        driver.execute_script("scrollBy(0, 400)")
        time.sleep(0.5)
        if i>5:
            break
        
    #to scroll down the page
    i=0
    while True:
        i+=1
        driver.execute_script("scrollBy(0, -400)")
        time.sleep(0.5)
        if i>2:
            break        
            
    driver.find_element(By.XPATH, "(//a[normalize-space()='HOME'])[1]").click()
    time.sleep(2) 
        
    #profile log out state        
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


