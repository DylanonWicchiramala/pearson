import selenium.common.exceptions as SeleniumExceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import keyboard
import sys
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://myenglishlab.pearson-intl.com/courses/content/1916134#!/1916134')


def login(username='63050131', retireTimes=5):
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


def expaned_tree(at=0):
    driver.implicitly_wait(3)
    sleep(0.5)
    tree = driver.find_elements_by_name('expand_more')
    tree[at].click()


def open_assignment(retireTimes=10, at=0):
    sleep(1)
    driver.implicitly_wait(10)  # delay for load assignment.
    print('openAssignment: opening assignment...')
    for i in range(retireTimes):
        try:
            open = driver.find_elements_by_link_text('Open')
            open[at].click()
            print('openAssignment: process done.')
            break

        except:
            print('openAssignment: clicking again.')
            sleep(1)

        if i == retireTimes - 1: print('openAssignment: something went wrong.')


def show_ans():
    link = driver.current_url
    ans_link = link + 'show_answers'

    # Open a new window
    driver.execute_script("window.open('');")
    # Switch to the new window and open URL B
    driver.switch_to.window(driver.window_handles[1])
    driver.get(ans_link)

    # driver.implicitly_wait(10)
    # try:
    #     show = driver.find_element_by_id('showAnswer')
    #
    #     #show ans in new tab
    #     webdriver.ActionChains(driver) \
    #         .key_down(Keys.CONTROL) \
    #         .click(show) \
    #         .key_up(Keys.CONTROL) \
    #         .perform()
    # except:
    #     show_ans()


def sunmit():
    driver.implicitly_wait(2)
    driver.find_element_by_id('submitButton').click()
    sleep(0.5)
    driver.find_element_by_id('continue').click()



def do_assignment():
    pass

def assignment_type():
    return assignment_type
    pass

def correct_chk():
    pass