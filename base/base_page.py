from selenium import webdriver


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.baidu.com/")