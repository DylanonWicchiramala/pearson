import time
from selenium import webdriver
import bs4
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from login_bot import login
from get_driver import driver
import sys

login()

sys.exit()

time.sleep(8)  # delays program for load website and login.
while True:
    time.sleep(1)
    try:
        break
    except:
        pass
