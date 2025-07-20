from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option('detach',True)

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(options=options,service=service)

driver.get("https://www.selenium.dev/documentation/")
driver.maximize_window()

mouse_click = driver.find_element(By.ID,"m-documentationwebdriver")

actions = ActionChains(driver)
actions.move_to_element(mouse_click).perform()
actions.click_and_hold().perform()
actions.release().perform()