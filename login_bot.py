from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

username = '63050131'  # type pearson user name here
try:
    psd = open('pwd.txt', 'r').read()  # create pwd.txt file and type your password
except:
    print('pwd.txt not found , please create pwd.txt file and type your password')

driver = webdriver.Chrome('C:/Users/Dylan/chromedriver_win32/chromedriver.exe')
driver.get("https://myenglishlab.pearson-intl.com/assignments/#!/allCourses/allStatuses")

sleep(2.9)  # delays for loading time.
loop_times = 1
while True:
    loop_times += 1
    try:
        print("Now logging... ")

        driver.find_element_by_name('name').send_keys(username)
        driver.find_element_by_name('password').send_keys(psd)
        driver.find_element_by_name('password').send_keys(Keys.RETURN)
        driver.maximize_window()
        break
    except:
        print("something wrong trying again...")
        sleep(0.2)
        if loop_times == 5: print('something went wrong.'); break
