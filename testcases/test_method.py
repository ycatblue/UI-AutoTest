# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBaidu:
    # 开始于每个方法始末（在类中）
    def setup_method(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        print("实例化浏览器并最大化")

    def teardown_method(self):
        driver.close()
        driver.quit()
        print("关闭浏览器")

    def test_baidu(self):
        driver.get("https://www.baidu.com/")
        title = driver.title
        url = driver.current_url
        text = driver.find_element(By.CSS_SELECTOR, 'a[href="http://news.baidu.com"]').text
        button_text = driver.find_element(By.ID, 'su').accessible_name
        assert title == "百度一下，你就知道"
        assert url == "https://www.baidu.com/"
        assert text == "新闻"

    def test_baidu2(self):
        driver.get("https://www.baidu.com/")
        title = driver.title
        url = driver.current_url
        text = driver.find_element(By.CSS_SELECTOR, 'a[href="http://news.baidu.com"]').text
        button_text = driver.find_element(By.ID, 'su').accessible_name
        assert title == "百度一下，你就知道"
        assert url == "https://www.baidu.com/"
        assert text == "新闻"
        assert button_text == "百度一下1"


if __name__ == '__main__':
    pytest.main()
