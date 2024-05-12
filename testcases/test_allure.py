from time import sleep

import allure
import pytest
from selenium.webdriver.common.by import By

from utils.read_yaml import read_yaml


class TestLogin:
    @pytest.mark.parametrize("username,password", read_yaml()['userinfo_list'])
    def test_login(self, driver, username, password):
        allure.dynamic.title("登录功能，账号为：" + username)
        driver.get("http://sellshop.5istudy.online/sell/user/login_page")
        driver.find_element(By.ID, 'username').send_keys(username)
        driver.find_element(By.ID, 'password').send_keys(password)
        driver.find_element(By.CSS_SELECTOR, '#login > form > p.login.button > input[type=submit]').click()
        if username == 'admin':
            text = driver.find_element(By.CSS_SELECTOR, "body > div > div > div > div > strong").text
            assert text == "用户不存在1"
        sleep(2)
