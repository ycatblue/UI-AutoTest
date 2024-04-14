# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import get_filepath

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/php/fileUpload.htm")
upload_file = driver.find_element(By.ID, 'file')
file_path = get_filepath.get_phone_path()
upload_file.send_keys(r"{}".format(file_path))
time.sleep(3)
driver.find_element(By.NAME, "submit").click()

time.sleep(3)
driver.close()
