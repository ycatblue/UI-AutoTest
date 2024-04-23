# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/clicks.htm")

element1 = driver.find_element(By.XPATH, "//input[@value='disable1']")
element2 = driver.find_element(By.XPATH, "//input[@value='Click me']")

print(element1.is_displayed())
print(element2.is_enabled())

element2.click()
print(element2.is_selected())
time.sleep(3)
driver.close()