from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

testname=['Rina','Ripa']
testuname=['rna','rpa']
testupassword=['121','0123']
testcon=['121','0123']
testic=['121','0123']
testemail=['rina@gmail.com','ripa@gmail.com']
testaddress=['abs','cbs']
gender='female'

def test_localhostLogin(testname,testuname,testupassword,testic,testemail,testcon,testaddress,i):
    driver.get("http://localhost/bookstore/index.php")
    # 2 | setWindowSize | 1214x647 | 
    driver.maximize_window()
    # 3 | click | name=submitButton | 
    driver.find_element(By.NAME, "submitButton").click()
    # 4 | click | name=name | 
    driver.find_element(By.NAME, "name").click()
    # 5 | type | name=name | maisha2
    driver.find_element(By.NAME, "name").send_keys(testname)
    # 6 | click | name=uname | 
    driver.find_element(By.NAME, "uname").click()
    # 7 | type | name=uname | maishaaa
    driver.find_element(By.NAME, "uname").send_keys(testuname)
    # 8 | click | name=upassword | 
    driver.find_element(By.NAME, "upassword").click()
    # 9 | type | name=upassword | 1234
    driver.find_element(By.NAME, "upassword").send_keys(testupassword)
    # 10 | click | name=ic | 
    driver.find_element(By.NAME, "ic").click()
    # 11 | type | name=ic | 1234
    driver.find_element(By.NAME, "ic").send_keys(testic)
    # 12 | click | name=email | 
    driver.find_element(By.NAME, "email").click()
    # 13 | type | name=email | m@gmail.com
    driver.find_element(By.NAME, "email").send_keys(testemail)
    # 14 | click | name=contact | 
    driver.find_element(By.NAME, "contact").click()
    # 15 | type | name=contact | 12345
    driver.find_element(By.NAME, "contact").send_keys(testcon)
    # 16 | click | css=form | 
    driver.find_element(By.CSS_SELECTOR, "form").click()
    # 17 | click | css=input:nth-child(35) | 
    driver.find_element(By.CSS_SELECTOR, "input:nth-child(35)").click()
    # 18 | click | name=address | 
    driver.find_element(By.NAME, "address").click()
    # 19 | type | name=address | abcd
    driver.find_element(By.NAME, "address").send_keys(testaddress)
    # 20 | click | name=submitButton | 
    driver.find_element(By.NAME, "submitButton").click()
    # 21 | close |  | 
    driver.close()

   # get_url= driver.current_url
    #   print("test- "+str(i)+" successfully logged in")
     #   driver.find_element(By.XPATH, "/html/body/header/blockquote/form[1]/input").click()
    #elif(get_url=="http://localhost/bookstore/login.php?errcode=1"):
        #print("test- "+str(i)+" failed to logged in")
    #else:
     #   print("something else happened")

lenofList=len(testname)
for i in range(0,lenofList):
    test_localhostLogin(testname[i],testuname[i],testupassword[i],testcon[i],testic[i],testemail[i],testaddress[i],i+1)
