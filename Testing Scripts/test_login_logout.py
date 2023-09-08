from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Specify the path to the ChromeDriver executable
service = Service(executable_path="D:\chromedriver\chromedriver.exe")

# Configure Chrome options
options = webdriver.ChromeOptions()

# Create a WebDriver instance
driver = webdriver.Chrome(service=service, options=options)


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
    
    #profile visitng state
    driver.find_element(By.XPATH, "(//a[normalize-space()='profile'])[1]").click()
    time.sleep(1)
    print("Profile Visit is Successful!")
    
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
    
    