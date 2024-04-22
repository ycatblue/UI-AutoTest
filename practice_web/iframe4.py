# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://sahitest.com/demo/iframesTest.htm")
driver.find_element(By.ID, 'checkRecord').clear()
driver.find_element(By.ID, 'checkRecord').send_keys("666")
time.sleep(3)

# 进入iframe
ele = driver.find_element(By.CSS_SELECTOR, 'body > iframe')
driver.switch_to.frame(ele)
driver.find_element(By.ID, "open-self").click()
time.sleep(3)
# 退出iframe,切换到上一级
# driver.switch_to.parent_frame()
# 切换到主界面
driver.switch_to.default_content()
driver.find_element(By.ID, 'checkRecord').clear()
driver.find_element(By.ID, 'checkRecord').send_keys("777")



time.sleep(3)
driver.close()