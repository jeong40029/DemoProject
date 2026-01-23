from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

service_obj = Service("/Users/haydenjeong/WebDrivers/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/abtest")
title_text = driver.find_element(By.CSS_SELECTOR, "h3").text
print(title_text)