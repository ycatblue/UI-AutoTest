# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
actions = ActionChains(driver)


def click_once():
    # 单击
    driver.get("https://sahitest.com/demo/clicks.htm")
    driver.find_element(By.NAME, 't2').send_keys("测试一下鼠标")
    time.sleep(2)

    # 使用鼠标功能的点击
    element = driver.find_element(By.NAME, 't1')
    ActionChains(driver).click(element).perform()
    time.sleep(2)
    driver.close()


def click_double():
    # 双击
    driver.get("https://sahitest.com/demo/clicks.htm")
    element = driver.find_element(By.XPATH, '/html/body/form/input[4]')
    ActionChains(driver).double_click(element).perform()
    time.sleep(2)
    driver.close()


def right_click():
    # 右击
    driver.get("https://sahitest.com/demo/clicks.htm")
    element = driver.find_element(By.XPATH, '/html/body/form/input[4]')
    ActionChains(driver).context_click(element).perform()
    time.sleep(2)
    driver.close()


def mouse_hover():
    # 悬浮
    driver.get("https://www.baidu.com/")
    element = driver.find_element(By.XPATH, '//*[@id="s-top-left"]/div/a')
    ActionChains(driver).move_to_element(element).perform()
    time.sleep(2)
    # 点击更多里的百科
    driver.find_element(By.XPATH, '//*[@id="s-top-more"]/div[3]/a/div').click()
    time.sleep(2)
    driver.close()


def drag_and_drop():
    # 拖动
    driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
    element_start = driver.find_element(By.ID, 'dragger')
    element_end = driver.find_element(By.XPATH, '/html/body/div[5]')
    ActionChains(driver).drag_and_drop(element_start, element_end).perform()
    time.sleep(2)
    driver.close()


def drag_and_drop_by_offset():
    # 拖动到坐标点
    driver.get('https://www.iviewui.com/view-ui-plus/component/form/slider')
    element_start = driver.find_element(By.XPATH, '//div[@class="ivu-slider-button"]')
    actions.drag_and_drop_by_offset(element_start, 200, 0).perform()
    time.sleep(3)
    driver.close()


if __name__ == '__main__':
    drag_and_drop_by_offset()
