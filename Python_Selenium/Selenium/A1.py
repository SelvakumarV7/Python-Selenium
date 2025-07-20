import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://practicetestautomation.com/practice-test-login/")
print("Browser Opened")

time.sleep(2)
browser.maximize_window()

title = browser.title           # It gives the Title of the webpage we given
print(title)
time.sleep(2)

username = browser.find_element(By.ID,"username")
username.send_keys("student")

password = browser.find_element(By.ID,"password")
password.send_keys("Password123")
time.sleep(1)

submit = browser.find_element(By.ID,"submit")
submit.click()
time.sleep(2)