from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option('detach',True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options,service=service)
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()

dd_element = driver.find_element(By.ID,"RESULT_RadioButton-9")
dd_element.click()

drop_down = Select(dd_element)
drop_down.select_by_visible_text("Evening")