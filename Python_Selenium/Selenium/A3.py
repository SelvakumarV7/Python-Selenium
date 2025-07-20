from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
url = "https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php"
browser.get(url)
browser.maximize_window()
time.sleep(2)

box = WebDriverWait(browser,10).until(
    EC.element_to_be_clickable((By.ID,"hobbies"))
)
box.click()
time.sleep(2)