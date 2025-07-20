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

user_name = driver.find_element(By.CSS_SELECTOR,"#username")
pass_word = driver.find_element(By.CSS_SELECTOR,"#password")

user_name.send_keys("student")
pass_word.send_keys("Password123")

log_in = driver.find_element(By.CSS_SELECTOR,"#submit")
log_in.click()

log_out = driver.find_element(By.CSS_SELECTOR,"#loop-container > div > article > div.post-content > div > div > div > a")
log_out.click()