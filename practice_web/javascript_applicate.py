# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def browser_operation():
    driver.get("https://www.baidu.com/")
    driver.execute_script('document.getElementById("kw").value="selenium"')
    driver.execute_script('document.getElementById("su").click')
    time.sleep(3)
    driver.close()


def browser_scroll():
    driver.get("https://news.baidu.com/")
    # 向下滑动200像素
    driver.execute_script("window.scrollTo(0,200)")
    time.sleep(2)

    # 滑动到底部
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(2)

    # 滑动到底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    driver.close()


def element_invisibility():
    driver.get("https://element.eleme.cn/#/zh-CN/component/form")
    element = driver.find_element(By.XPATH, "//span[@class='el-radio__inner']")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)
    driver.close()


if __name__ == '__main__':
    browser_scroll()
