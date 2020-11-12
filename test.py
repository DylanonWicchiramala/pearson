import time
from selenium import webdriver
import bs4
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome('C:/Users/Dylan/chromedriver_win32/chromedriver.exe')

driver.get('https://myenglishlab.pearson-intl.com/assignments/#!/allCourses/allStatuses')

time.sleep(10)   # login time.
while True:
    try:
        #time.sleep()
        driver.find_element_by_class_name('accordion-link ng-binding ng-scope ng-isolate-scope').click()
        print("pressed button.")
        break
    except:
        time.sleep(2)
        print("skipped.")