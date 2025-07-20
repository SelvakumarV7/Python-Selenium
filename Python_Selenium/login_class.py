from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option('detach',True)

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(options=options,service=service)

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

user_name = driver.find_element(By.TAG_NAME,"input")
pass_word = driver.find_element(By.ID,"password")
log_in = driver.find_element(By.CLASS_NAME,"btn")

user_name.send_keys("student")
pass_word.send_keys("Password123")
log_in.click()