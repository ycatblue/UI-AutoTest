# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
driver.get("https://element.eleme.cn/#/zh-CN/component/cascader")
# 根据同级定位
driver.find_element(By.XPATH, "//span[text()='默认 click 触发子菜单']/following-sibling::div/div/input").click()


time.sleep(3)
driver.close()