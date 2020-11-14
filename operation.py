import selenium.common.exceptions as SeleniumExceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from get_driver import driver
import keyboard
import sys


def login(username='63050131', retireTimes=10):
    # get usermname and password
    username = username
    try:
        pwd = open('pwd.txt', 'r').read()  # create pwd.txt file and type your password
    except:
        print('pwd.txt not found, please create pwd.txt file and type your password in it.')

    # login
    driver.implicitly_wait(10)  # delays for loading time.
    print("login: Now logging...")
    for i in range(retireTimes):
        try:
            driver.find_element_by_name('name').send_keys(username)
            driver.find_element_by_name('password').send_keys(pwd)
            driver.find_element_by_name('password').send_keys(Keys.RETURN)
            print('logging: process done.')
            break
        except:
            print("logging: logging again.")
            sleep(0.7)
        if i == retireTimes - 1: print('logging: something went wrong.')


def open_assignment(retireTimes=10, at=1):
    at = at - 1
    sleep(1)
    driver.implicitly_wait(10)  # delay for load assignment.
    print('openAssignment: opening assignment...')
    for i in range(retireTimes):
        try:
            driver.find_element_by_link_text('Resume').click()
            print('openAssignment: process done.')
            break

        except SeleniumExceptions.NoSuchElementException:
            driver.find_element_by_link_text('Open').click()
            print('openAssignment: process done.')
            break

        except:
            print('openAssignment: clicking again.')
            sleep(1)

        if i == retireTimes - 1: print('openAssignment: something went wrong.')

def do_assignment():
    assignment_type = assignment_type()
    pass

def assignment_type():
    return assignment_type
    pass

def correct_chk():
    pass