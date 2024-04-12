# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.iviewui.com/view-ui-plus/component/form/radio")
# driver.find_elements(By.XPATH, '//input[@type="radio" and @class="ivu-radio-input"]')[1].click()
# time.sleep(1)
# driver.find_elements(By.XPATH, '//input[@type="radio" and @class="ivu-radio-input"]')[2].click()
# time.sleep(1)
# driver.find_elements(By.XPATH, '//input[@type="radio" and @class="ivu-radio-input"]')[3].click()
# driver.find_element(By.XPATH, '//span[text()="Android"]').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//span[text()="Windows"]').click()
driver.find_element(By.XPATH, '//span[text()="Android"]/preceding-sibling::span/input').click()
time.sleep(3)
driver.close()