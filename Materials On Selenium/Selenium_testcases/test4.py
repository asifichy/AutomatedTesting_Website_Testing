from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

testSuiteUsername=['maisha','ruhin']
testSuitePassword=['1234','12345678']

def test_localhostLogin(username,password,i):


    driver.get("http://localhost/bookstore/index.php")
    time.sleep(3)
    #  setWindowSize | 1920x1040 | 
    #driver.set_window_size(1920, 1040)
    # Maximize 
    driver.maximize_window()
    #  click | xpath=(//input[@name='submitButton'])[2] 
    driver.find_element(By.XPATH, "(//input[@name=\'submitButton\'])[2]").click()
    #  click | xpath=//input[@name='username'] | 
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@name=\'username\']").click()
    #  type | xpath=//input[@name='username'] | mm
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@name=\'username\']").send_keys(username)
    #  click | xpath=//input[@name='pwd'] | 
    driver.find_element(By.XPATH, "//input[@name=\'pwd\']").click()
    #  type | xpath=//input[@name='pwd'] | 123
    driver.find_element(By.XPATH, "//input[@name=\'pwd\']").send_keys(password)
    #  click | xpath=//input[@name='submitButton'] | 
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    time.sleep(3)

    get_url= driver.current_url
    if(get_url=="http://localhost/bookstore/index.php"):
        print("test- "+str(i)+" successfully logged in")
       # driver.find_element(By.XPATH, "/html/body/header/blockquote/form[1]/input").click()
        driver.find_element(By.XPATH, "//input[@value='Logout']").click()
    elif(get_url=="http://localhost/bookstore/login.php?errcode=1"):
        print("test- "+str(i)+" failed to logged in")
    else:
        print("something else happened")
lenofList=len(testSuiteUsername)
for i in range(0,lenofList):
    test_localhostLogin(testSuiteUsername[i],testSuitePassword[i],i+1)