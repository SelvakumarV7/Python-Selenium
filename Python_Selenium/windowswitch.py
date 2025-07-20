from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option('detach',True)

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(options=options,service=service)

driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()

main_window = driver.current_window_handle
main_window_title = driver.title

click_HomePage = driver.find_element(By.XPATH,'//*[@id="Tabbed"]/a/button')
click_HomePage.click()

for handle in driver.window_handles:
    if handle != main_window:
        driver.switch_to.window(handle)
        break

child_window = driver.title
time.sleep(5)
driver.close()