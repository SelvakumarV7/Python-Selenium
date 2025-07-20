from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
url = "https://practice.expandtesting.com/hovers"
browser.get(url)
browser.maximize_window()
time.sleep(2)

mouse = ActionChains(browser)
hover = browser.find_element(By.XPATH,'//*[@id="core"]/div/div/div[1]/img')
mouse.move_to_element(hover).perform()
time.sleep(2)

hover = browser.find_element(By.XPATH,'//*[@id="core"]/div/div/div[2]/img')
mouse.move_to_element(hover).perform()
time.sleep(2)

hover = browser.find_element(By.XPATH,'//*[@id="core"]/div/div/div[3]/img')
mouse.move_to_element(hover).perform()
time.sleep(2)

drop = WebDriverWait(browser,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="examples-dropdown"]'))
)
mouse.click(drop).perform()
time.sleep(2)

right_click = browser.find_element(By.XPATH,'//*[@id="main-navbar"]/ul[1]/li[5]/a')
mouse.context_click(right_click).perform()
time.sleep(2)