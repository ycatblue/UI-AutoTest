# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/alertTest.htm")
driver.find_element(By.NAME, 'b1').click()
time.sleep(3)
driver.switch_to.alert.accept()

time.sleep(3)
driver.close()
