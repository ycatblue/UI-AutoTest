# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file://E:/UI-AutoTest/HTML/iframe_test.html")
driver.find_element(By.ID, 'checkRecord').clear()
driver.find_element(By.ID, 'checkRecord').send_keys("777")
time.sleep(3)
# 使用id定位iframe
# driver.switch_to.frame("iframe_id")
# 使用name定位iframe
driver.switch_to.frame("iframe_name")
driver.find_element(By.XPATH, "//span[text()='番剧']").click()
time.sleep(3)
driver.close()