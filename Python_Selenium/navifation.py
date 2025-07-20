from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.add_experimental_option('detach',True)

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service = service,options=options)

driver.get("https://www.google.com/")

driver.maximize_window()

driver.quit()

