from time import sleep
from selenium import webdriver
import bs4
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome('C:/Users/Dylan/chromedriver_win32/chromedriver.exe')

driver.get('https://www.youtube.com/?gl=TH&hl=th')
for i in range(100):
    try:
        name_1 = driver.find_elements_by_id('video-title')  #ssssssssssssssss
        break
    except:
        sleep(0.1)
        print(i)

for i in range
    print(name_1[i].text)