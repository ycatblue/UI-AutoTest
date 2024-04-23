# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://baidu.com/")
element1 = driver.find_element(By.CSS_SELECTOR, 'a[href="http://news.baidu.com"]')
element2 = driver.find_element(By.ID, "su")
element3 = driver.find_element(By.XPATH, '//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]')

print(element1.text)
print(element2.accessible_name)
print(element3.text)
time.sleep(3)
driver.close()