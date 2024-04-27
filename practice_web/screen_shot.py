# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from utils.get_filepath import get_screen_shot_path

driver = webdriver.Chrome()
driver.get("https://news.baidu.com/")
driver.maximize_window()

# element = driver.find_element()
driver.save_screenshot(get_screen_shot_path())

time.sleep(3)
driver.close()