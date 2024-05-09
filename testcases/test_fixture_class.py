# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


class TestBaidu:
    def test_baidu(self, driver):
        driver.get("https://www.baidu.com")
        title = driver.title
        assert title == "百度一下，你就知道"

    def test_baidu1(self, driver):
        driver.get("https://www.baidu.com")
        title = driver.title
        assert title == "百度一下"


if __name__ == '__main__':
    pytest.main()