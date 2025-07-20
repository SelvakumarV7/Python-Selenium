from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option('detach',True)

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(options=options,service=service)

driver.get("https://www.w3schools.com/Html/html5_draganddrop.asp")
driver.maximize_window()

time.sleep(3)

drag_element = driver.find_element(By.ID,"img1")
drop_element = driver.find_element(By.ID,"div2")

actions = ActionChains(driver)
actions.click_and_hold(drag_element).move_to_element(drop_element)
actions.release().perform()