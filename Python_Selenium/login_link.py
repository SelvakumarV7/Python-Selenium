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

user_name = driver.find_element(By.NAME,"username")
pass_word = driver.find_element(By.NAME,"password")
log_in = driver.find_element(By.XPATH,'//button[@id="submit"]')

user_name.send_keys("student")
pass_word.send_keys("Password123")
log_in.click()

# open_acc = driver.find_element(By.LINK_TEXT,"Open New Account")
# open_acc.click()
# print("open account clicked")
#
# fund_transfer = driver.find_element(By.PARTIAL_LINK_TEXT,"Transfer")
# fund_transfer.click()
# print("printed fund transfer page")