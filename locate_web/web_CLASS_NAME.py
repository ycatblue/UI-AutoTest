# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.bilibili.com/")
driver.find_element(By.CLASS_NAME, 'nav-search-input').send_keys("selenium")
driver.find_element(By.CLASS_NAME, 'nav-search-btn').click()
time.sleep(3)
driver.close()