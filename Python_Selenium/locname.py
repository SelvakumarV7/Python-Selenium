from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach',True)

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service,options=options)

driver.get("https://demo.applitools.com/")

driver.maximize_window()

user_name = driver.find_element(By.ID,'username')

user_name.send_keys("Selvakumar")