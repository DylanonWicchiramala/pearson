from time import sleep
from selenium import webdriver
import bs4
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome('C:/Users/Dylan/chromedriver_win32/chromedriver.exe')

driver.get('https://www.google.com')
w = driver.current_window_handle
w0 = driver.window_handles
driver.switch_to_window(w0[1])
