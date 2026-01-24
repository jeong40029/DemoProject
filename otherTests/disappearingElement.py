from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import none_of

service_obj = Service("/Users/haydenjeong/WebDrivers/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/disappearing_elements")
attempts = 0
max_attempts = 10
found_element = None

while attempts < max_attempts:
    elements = driver.find_elements(By.LINK_TEXT, "Gallery")

    if len(elements) > 0:
        found_element = elements[0]
        print(f"Found the element after {attempts + 1} attempts")
        break

    driver.refresh()
    attempts += 1

assert found_element is not None, f"Cannot find the element after {max_attempts} attempts"
