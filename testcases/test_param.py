# -*- coding: utf-8 -*-
import time

import pytest
from selenium.webdriver.common.by import By


# 单个参数循环
@pytest.mark.parametrize("username", ["user1", "user2"])
def test_param_single(username):
    print("用户名为：{}".format(username))


# 多个参数循环
@pytest.mark.parametrize(["username", "password"], [("admin", "123456"), ("test01", "123456")])
def test_param_multiple(driver, username, password):
    driver.get("http://sellshop.5istudy.online/sell/user/login_page")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//input[@value='登录']").click()
    time.sleep(2)


# 字典形式传参
@pytest.mark.parametrize("data", [{"username": "admin", "password": "123456"}, {"username": "test01", "password": "123456"}])
def test_param_dict(driver, data):
    driver.get("http://sellshop.5istudy.online/sell/user/login_page")
    driver.find_element(By.ID, "username").send_keys(data["username"])
    driver.find_element(By.ID, "password").send_keys(data["password"])
    driver.find_element(By.XPATH, "//input[@value='登录']").click()
    time.sleep(2)

