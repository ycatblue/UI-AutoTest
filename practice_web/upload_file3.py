# -*- coding: utf-8 -*-
import time
from pywinauto import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com/')
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="form"]/span[1]/span[1]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//input[@class="upload-pic"]').click()
time.sleep(2)
keyboard.send_keys(r"E:\UI-AutoTest\files\01400.jpg")
time.sleep(5)
keyboard.send_keys("{ENTER}")

time.sleep(3)
driver.close()
