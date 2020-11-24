import time
from selenium import webdriver
import bs4
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
#import operation
import operation_test_unit as test

test.login()
test.expaned_tree()
test.open_assignment(at= 0)
test.show_ans()