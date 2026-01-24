from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/haydenjeong/WebDrivers/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
actions = ActionChains(driver)

driver.get("https://the-internet.herokuapp.com/drag_and_drop")

column_a = driver.find_element(By.CSS_SELECTOR, "#column-a")
column_b = driver.find_element(By.CSS_SELECTOR, "#column-b")

actions.drag_and_drop(column_a, column_b).perform()
newColumnA_header = column_a.find_element(By.TAG_NAME, "header").text
newColumnB_header = column_b.find_element(By.TAG_NAME, "header").text

assert newColumnA_header == "B"
assert newColumnB_header == "A"