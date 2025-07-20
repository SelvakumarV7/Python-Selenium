from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
url = "https://practicetestautomation.com/practice-test-login/"
browser.get(url)
browser.maximize_window()
time.sleep(2)

username = browser.find_element(By.XPATH,'//*[@id="username"]')
username.send_keys("student")
time.sleep(2)

browser.back()
time.sleep(2)

browser.forward()
time.sleep(2)

browser.refresh()
time.sleep(2)