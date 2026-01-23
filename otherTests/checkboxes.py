from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/haydenjeong/WebDrivers/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/checkboxes")

checkboxes = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input")

if not checkboxes[0].is_selected():
    checkboxes[0].click()
    print("The first checkbox is checked.")

if checkboxes[1].is_selected():
    checkboxes[1].click()
    print("The second checkbox is unchecked.")

assert checkboxes[0].is_selected() is True
assert checkboxes[1].is_selected() is False

driver.quit()