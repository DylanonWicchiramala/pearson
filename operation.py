from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from get_driver import driver
import keyboard
import sys


# driver = webdriver.Chrome('C:/Users/Dylan/chromedriver_win32/chromedriver.exe')
# driver.get("https://myenglishlab.pearson-intl.com/assignments/#!/allCourses/allStatuses")

def login(username='63050131', retireTimes=10):
    # get usermname and password
    username = username  # type pearson user name here
    try:
        pwd = open('pwd.txt', 'r').read()  # create pwd.txt file and type your password
    except:
        print('pwd.txt not found, please create pwd.txt file and type your password in it.')

    # login
    sleep(2.9)  # delays for loading time.
    loop_times = 1
    print("login: Now logging...")
    for i in range(retireTimes):
        loop_times += 1
        try:
            driver.find_element_by_name('name').send_keys(username)
            driver.find_element_by_name('password').send_keys(pwd)
            driver.find_element_by_name('password').send_keys(Keys.RETURN)
            break
        except:
            print("login: logging again.")
            sleep(0.7)
    if i == retireTimes - 1: ('login: something went wrong.')
    sleep(7.1)  # assignment loadding time
    print('loggin: process done.')


def openAssignment(retireTimes=50, at=1):
    at = at - 1
    #sleep(7)  # delay for load assignment.
    print('openAssignment: clicking Ex.')
    #driver.get('https://myenglishlab.pearson-intl.com/assignments/#!/allCourses/allStatuses')
    for i in range(retireTimes):
        try:
            open = driver.find_element_by_id('accordion-link ng-binding ng-scope ng-isolate-scope')
            open.get_attribute('href')
            break
        except:
            print('openAssignment: clicking again.')
            sleep(1)
    if i == retireTimes - 1: print('openAssignment: something went wrong.')
    print('openAssignment: process done.')
