from selenium.webdriver.common.by import By
from selenium import webdriver

from base.base_page import BasePage


class PageBaidu(BasePage):
    # 新闻
    news = (By.CSS_SELECTOR, 'a[href="http://news.baidu.com"]')
    # 百度一下按钮
    button = (By.ID, 'su')
    # 百度输入框
    input = (By.ID, 'kw')

    def search_keyword(self, keyword):
        self.driver.find_element(*self.input).send_keys(keyword)
        self.driver.find_element(*self.button).click()
        self.driver.implicitly_wait(10)