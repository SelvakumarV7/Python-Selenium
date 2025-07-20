from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

browser = webdriver.Chrome()
url = "https://jqueryui.com/"
browser.get(url)
browser.maximize_window()
time.sleep(2)

links = browser.find_elements(By.TAG_NAME,"a")
total_links = len(links)
print(total_links)

for i in links:
    href = i.get_attribute('href')
    if href:
        try:
            response = requests.get(href,timeout=1)
            if response.status_code>=400:
                print(f"broken links: {href}(status code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"error accessing {href}: {e}")