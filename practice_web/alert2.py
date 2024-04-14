# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/confirmTest.htm")
driver.find_element(By.NAME, 'b1').click()
time.sleep(2)
# 点击确定
# driver.switch_to.alert.accept()
# 点击取消
driver.switch_to.alert.dismiss()
time.sleep(3)
driver.close()
