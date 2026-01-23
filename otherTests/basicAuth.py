from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/haydenjeong/WebDrivers/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

user_id = "admin"
user_pw = "admin"

url = f"https://{user_id}:{user_pw}@the-internet.herokuapp.com/basic_auth"

driver.get(url)
msg = driver.find_element(By.XPATH, "//p").text
assert "Congratulations!" in msg
