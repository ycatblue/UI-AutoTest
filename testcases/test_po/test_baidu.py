# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from page.page_baidu import PageBaidu


class TestBaidu:
    def test_baidu(self, driver):
        page = PageBaidu()

        # 登录测试
        driver.get("https://www.baidu.com/")
        title = driver.title
        url = driver.current_url
        text = driver.find_element(*page.news).text
        button_text = driver.find_element(*page.button).accessible_name
        assert title == "百度一下，你就知道"
        assert url == "https://www.baidu.com/"
        assert text == "新闻"

    def test_baidu2(self, driver):
        # 未登录测试
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
