# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://sellshop.5istudy.online/sell/user/login_page")
# 输入账号
driver.find_element(By.ID, "username").send_keys("ycatblue")
# 输入密码
driver.find_element(By.ID, "password").send_keys("hml123")
# 登录
driver.find_element(By.XPATH, "//input[@value='登录']").click()
# 新增
driver.find_element(By.LINK_TEXT, "新增").click()
# 输入名称
driver.find_element(By.NAME, "productName").send_keys("菲力牛排")
# 输入价格
driver.find_element(By.NAME, "productPrice").send_keys("122")
# 输入名称
driver.find_element(By.NAME, "productStock").send_keys("66")
# 输入库存
driver.find_element(By.NAME, "productDescription").send_keys("好吃又新鲜")
# 输入描述
driver.find_element(By.NAME, "productDescription").send_keys("好吃又新鲜")
# 图片链接
driver.find_element(By.NAME, "productIcon").send_keys(
    "http://admin.5istudy.online/media/goods/images/7_P_1448945104883.jpg")

# 选择类目
select_type = Select(driver.find_element(By.NAME, "categoryType"))
select_type.select_by_value("6")

# 提交
driver.find_element(By.XPATH, '//*[@id="page-content-wrapper"]/div/div/div/form/button').click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, 'a[href="/sell/seller/product/list"]').click()
time.sleep(3)
driver.close()
