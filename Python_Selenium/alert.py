from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option('detach',True)

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(options=options,service=service)

driver.get("https://www.selenium.dev/documentation/webdriver/interactions/alerts/")
driver.maximize_window()

alert_text = driver.find_element(By.XPATH,"/html/body/div/div[1]/div/main/div/p[2]/a")
alert_text.click()

time.sleep(3)
alert = Alert(driver)
alert.accept()
