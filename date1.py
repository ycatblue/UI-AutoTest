# -*- coding: utf-8 -*-
import time
import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.iviewui.com/view-ui-plus/component/form/date-picker")
current_date = datetime.date.today()
formatted_date = current_date.strftime("%Y-%m-%d")
one_year_ago = current_date.replace(year=current_date.year - 1)
formatted_date2 = one_year_ago.strftime("%Y-%m-%d")
date_range = formatted_date + " - " + formatted_date2

driver.find_element(By.XPATH, '//input[@class="ivu-input ivu-input-default '
                              'ivu-input-with-suffix"]').send_keys(formatted_date2)
driver.find_elements(By.XPATH, '//input[@class="ivu-input ivu-input-default '
                              'ivu-input-with-suffix"]')[1].send_keys(date_range)
time.sleep(3)
driver.close()
