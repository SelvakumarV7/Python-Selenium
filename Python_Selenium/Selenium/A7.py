from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

browser = webdriver.Chrome()

browser.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
browser.maximize_window()
time.sleep(2)

browser.switch_to.new_window()
time.sleep(2)

browser.get("https://www.saucedemo.com/")
browser.maximize_window()
time.sleep(2)

first_tab = browser.window_handles[0]
browser.switch_to.window(first_tab)
time.sleep(2)