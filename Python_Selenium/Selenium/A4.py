from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
url = "https://demo.automationtesting.in/Alerts.html"
browser.get(url)
browser.maximize_window()
time.sleep(2)

alert = WebDriverWait(browser,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="OKTab"]/button'))
)
alert.click()
time.sleep(2)

pop = browser.switch_to.alert
pop.accept()
time.sleep(2)

cancel_alert = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a')
cancel_alert.click()
time.sleep(2)

c_click =WebDriverWait(browser,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="CancelTab"]/button'))
)
c_click.click()
pop1 = browser.switch_to.alert
pop1.accept()
time.sleep(2)

c_click.click()
pop2 = browser.switch_to.alert
pop2.dismiss()
time.sleep(2)

box = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a')
box.click()
time.sleep(2)

text_click = WebDriverWait(browser,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="Textbox"]/button'))
)
text_click.click()
pop3 = browser.switch_to.alert
pop3.send_keys("SelvaSweet")
pop3.accept()
time.sleep(3)