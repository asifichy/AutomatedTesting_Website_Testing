# Generated by Selenium IDE
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestBooks():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_books(self):
    self.driver.get("http://localhost/bookstore/index.php")
    self.driver.set_window_size(691, 720)
    self.driver.find_element(By.CSS_SELECTOR, ".hf:nth-child(3) > .hi").click()
    self.driver.find_element(By.NAME, "username").click()
    self.driver.find_element(By.NAME, "username").send_keys("ruhin")
    self.driver.find_element(By.NAME, "pwd").click()
    self.driver.find_element(By.NAME, "pwd").send_keys("12345678")
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(9)").click()
    self.driver.close()
    self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > table .button").click()
    self.driver.find_element(By.NAME, "checkout").click()
    self.driver.find_element(By.CSS_SELECTOR, ".button").click()
    self.driver.find_element(By.NAME, "submitButton").click()
    self.driver.close()
  