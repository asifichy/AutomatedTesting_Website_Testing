from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

"""test_username = ["Asif Niloy"]
test_email = ["asif@gmail.com"]
test_number = ["01620833383"]
test_password = ["111"]
test_confPassword = ["111"]"""

"""test_username = ["Shafika"]
test_email = ["shafika@gmail.com"]
test_number = ["01600000000"]
test_password = ["111"]
test_confPassword = ["111"]"""

test_username = ["Prianka"]
test_email = ["prianka@gmail.com"]
test_number = ["01600000000"]
test_password = ["111"]
test_confPassword = ["111"]

def test_localhost_signup(username, email, number, password, confPassword, i):
    #opening the webpage
    driver.get("http://localhost/TheGrindCoffeeWebApplication/home.php")
    time.sleep(3)
    
    driver.maximize_window()

    # Test the signup page
        
    #clicking on account button
    driver.find_element(By.XPATH, "(//div[@id='user-btn'])[1]").click()

    #clicking on login button
    driver.find_element(By.XPATH, "(//a[normalize-space()='login'])[1]").click()

    #clicking on register button
    driver.find_element(By.XPATH, "(//a[normalize-space()='register now'])[1]").click()

    # Finding the input fields and submit button
    username_input = driver.find_element(By.XPATH, "(//input[@placeholder='enter your name'])[1]")
    email_input = driver.find_element(By.XPATH, "(//input[@placeholder='enter your email'])[1]")
    number_input = driver.find_element(By.XPATH, "(//input[@placeholder='enter your number'])[1]")
    password_input = driver.find_element(By.XPATH, "(//input[@placeholder='enter your password'])[1]")
    confPass_input = driver.find_element(By.XPATH, "(//input[@placeholder='confirm your password'])[1]")

    # Input test data
    username_input.send_keys(username)     
    email_input.send_keys(email)
    number_input.send_keys(number)
    password_input.send_keys(password)
    confPass_input.send_keys(confPassword)

    #Submit the data
    registerBtn = driver.find_element(By.XPATH, "(//input[@name='submit'])[1]")
    registerBtn.click() 

    time.sleep(3)

    #driver.implicitly_wait(2)

    # Check if a success message is displayed
    #success_message = driver.find_element_by_id("success-message")      
    #if success_message.is_displayed():
    #    print("Signup test PASSED: User successfully signed up.")
    #else:
    #    print("Signup test FAILED: User not signed up or success message not found.")        

    get_url = driver.current_url
    if(get_url == "http://localhost/TheGrindCoffeeWebApplication/home.php"):
        print("test- " + str(i) + " successfully signed in!")
        
        driver.find_element(By.XPATH, "(//div[@id='user-btn'])[1]").click()
        driver.find_element(By.XPATH, "(//a[normalize-space()='profile'])[1]").click()
        time.sleep(3)
    else:
        print("Failed to signed in!")      
        print("An error occurred during signup testing!\n")
        
lenOfList = len(test_username)
for i in range(0, lenOfList):
    test_localhost_signup(test_username[i], test_email[i], test_number[i], test_password[i], test_confPassword[i], i+1)
    
    