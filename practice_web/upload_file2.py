# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pywinauto import keyboard

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.iviewui.com/view-ui-plus/component/form/upload")
driver.find_element(By.XPATH, "//button[@class='ivu-btn ivu-btn-default']").click()
time.sleep(3)
keyboard.send_keys(r"E:\UI-AutoTest\files\01400.jpg")
time.sleep(5)
keyboard.send_keys('{ENTER}')

time.sleep(5)
driver.close()
