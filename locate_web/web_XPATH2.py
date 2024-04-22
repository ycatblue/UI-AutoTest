# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
driver.get("https://www.baidu.com/")
# 绝对路径
# driver.find_element(By.XPATH, "/html/body/div/div/div[3]/a").click()
# 根据ID定位
# driver.find_element(By.XPATH, "//input[@id='kw']").send_keys('selenium')
# 根据class定位
# driver.find_element(By.XPATH, "//input[@class='s_ipt']").send_keys('selenium')
# 根据name定位
# driver.find_element(By.XPATH, "//input[@name='wd']").send_keys('selenium')
# 多个属性组合定位
# driver.find_element(By.XPATH, "//input[@name='wd' and @class='s_ipt' and @autocomplete='off']").send_keys('selenium')
# 多组数据使用下标定位
# driver.find_element(By.XPATH, "//div[@id='s-top-left']/a[4]").click()
# 根据span文本内容
# driver.find_element(By.XPATH, '//span[text() = "武汉大学官宣"]').click()
# 根据同级弟弟定位
# driver.find_element(By.XPATH,
#                     "//a[text()='新闻' and @class='mnav c-font-normal c-color-t']/following-sibling::a[3]").click()
# 根据同级哥哥定位
driver.find_element(By.XPATH, "//a[text()='贴吧' and @class='mnav c-font-normal c-color-t']/preceding-sibling::a[3]").click()

time.sleep(3)
driver.close()