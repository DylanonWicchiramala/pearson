import time
from selenium import webdriver
import bs4
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome('C:/Users/Dylan/chromedriver_win32/chromedriver.exe')

driver.get('https://myenglishlab.pearson-intl.com/assignments/#!/allCourses/allStatuses')

time.sleep(8)  # delays program for load website and login.
while True:
    time.sleep(1)
    try:
        break
    except:
        pass
