from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from get_driver import driver
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
    sleep(7)  # assignment loadding time
    print('loggin: process done.')


def openAssignment(retireTimes=50, at=1):
    at = at - 1
    sleep(3)  # delay for load assignment.
    print('openAssignment: clicking Ex.')
    for i in range(retireTimes):
        try:
            driver.find_element_by_id('timeline-item-link').get_attribute('herf') #get herf
            break
        except:
            print('openAssignment: clicking again.')
            sleep(0.7)
    if i == retireTimes - 1: print('openAssignment: something went wrong.')
    print('openAssignment: process done.')
