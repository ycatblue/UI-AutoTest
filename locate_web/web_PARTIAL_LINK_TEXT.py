# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
driver.get("https://www.baidu.com/")
driver.find_element(By.PARTIAL_LINK_TEXT, "闻").click()
# driver.find_elements(By.PARTIAL_LINK_TEXT, "新闻")[0].click()
time.sleep(3)
driver.close()
