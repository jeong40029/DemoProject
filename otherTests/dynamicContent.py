from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/haydenjeong/WebDrivers/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
actions = ActionChains(driver)

max_retries = 3
is_changed = False

driver.get("https://the-internet.herokuapp.com/dynamic_content")

original_text = driver.find_elements(By.XPATH, "//div[@class='large-10 columns']")[0].text

for i in range(max_retries):
    driver.refresh()
    new_text = driver.find_elements(By.XPATH, "//div[@class='large-10 columns']")[0].text

    if original_text != new_text:
        is_changed = True
        break

assert is_changed == True