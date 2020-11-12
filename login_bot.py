from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from get_driver import driver
import sys


# driver = webdriver.Chrome('C:/Users/Dylan/chromedriver_win32/chromedriver.exe')
# driver.get("https://myenglishlab.pearson-intl.com/assignments/#!/allCourses/allStatuses")

def login(username='63050131'):
    # get usermname and password
    username = username  # type pearson user name here
    try:
        pwd = open('pwd.txt', 'r').read()  # create pwd.txt file and type your password
    except:
        print('pwd.txt not found , please create pwd.txt file and type your password')

    # login
    sleep(2.9)  # delays for loading time.
    loop_times = 1
    print("Now logging...")
    while True:
        loop_times += 1
        try:
            driver.find_element_by_name('name').send_keys(username)
            driver.find_element_by_name('password').send_keys(pwd)
            driver.find_element_by_name('password').send_keys(Keys.RETURN)
            driver.maximize_window()
            break
        except:
            #print("trying again.")
            sleep(0.7)

        if loop_times == 10:
            print('something went wrong.')
            break