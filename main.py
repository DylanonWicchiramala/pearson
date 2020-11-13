import time
from selenium import webdriver
import bs4
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import operation
from get_driver import driver
import sys
from time import sleep

operation.login()
#driver.maximize_window()
input("press any key to continue.")
operation.openAssignment()