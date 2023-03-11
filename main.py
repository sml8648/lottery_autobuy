from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
from datetime import datetime
from tabulate import tabulate
if __name__ == '__main__':

    dt = datetime.today().strftime('%Y-%m-%d')

    url = 'https://dhlottery.co.kr/common.do?method=main'
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url)
