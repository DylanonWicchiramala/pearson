from selenium import webdriver
#from BeautifulSoup import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('C:/Users/Dylan/chromedriver_win32/chromedriver.exe')
driver.get('https://myenglishlab.pearson-intl.com/assignments/#!/allCourses/allStatuses')
