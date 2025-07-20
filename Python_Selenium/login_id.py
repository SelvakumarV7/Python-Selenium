from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option('detach',True)

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(options=options, service=service)

driver.get("https://demo.applitools.com/")

driver.maximize_window()

user_name = driver.find_element(By.ID,"username")
pass_word = driver.find_element(By.ID,"password")

user_name.send_keys("Selvakumar")
pass_word.send_keys("123456")

log_in = driver.find_element(By.ID,"log-in")

log_in.click()