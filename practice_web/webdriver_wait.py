# -*- coding: utf-8 -*-
import os
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.get_filepath import download_file_path
from selenium import webdriver
from selenium.webdriver.common.by import By


path = download_file_path() + "/LATEST_RELEASE"
if os.path.exists(path):
    print("文件存在")
    os.remove(path)
    print("文件已删除")

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory": "{}".format(download_file_path())}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chromeOptions)
driver.maximize_window()
driver.get("https://registry.npmmirror.com/binary.html?path=chromedriver/")
locate = (By.XPATH, '/html/body/table/tbody/tr[156]/td[2]/a')
element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locate), '找不到元素')
element.click()
time.sleep(3)
driver.close()
