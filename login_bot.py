from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

usrname = '63050131'
psd = "hW2urmitfq"

driver = webdriver.Chrome('C:/Users/Dylan/chromedriver_win32/chromedriver.exe')
driver.get("https://myenglishlab.pearson-intl.com/assignments/#!/allCourses/allStatuses")

sleep(2.9)    #loading time
loop_times = 1
while True:
    if loop_times==4 : break
    try:
        print("Now logging... ")

        driver.find_element_by_name('name').send_keys(usrname)
        sleep(0.03)
        driver.find_element_by_name('password').send_keys(psd)
        driver.find_element_by_name('password').send_keys(Keys.RETURN)
        driver.maximize_window()
        break
    except:
        print("some thing wrong trying again...")
        sleep(0.2)