from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome()
url ="https://www.saucedemo.com/"
browser.get(url)
browser.maximize_window()
time.sleep(2)

username = browser.find_element(By.ID,"user-name")
username.send_keys("Selvakumareaaaaaa")
time.sleep(2)

mouse = ActionChains(browser)

mouse.click(username).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
time.sleep(2)

mouse.send_keys(Keys.ESCAPE).perform()
time.sleep(2)

username = browser.find_element(By.ID,"user-name")
username.send_keys("Selvakumar")
time.sleep(2)