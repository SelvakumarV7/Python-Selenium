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

user_name = driver.find_element(By.XPATH,'//input[@type="text"]')
pass_word = driver.find_element(By.XPATH,'//*[@id="password"]')
submit = driver.find_element(By.XPATH,'/html/body/div/div/section/section/div[1]/button')


user_name.send_keys("student")
pass_word.send_keys("Password123")
submit.click()

log_out = driver.find_element(By.XPATH,"/html/body/div/div/section/div/div/article/div[2]/div/div/div/a")
log_out.click()
