from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

service_obj = Service("/Users/haydenjeong/WebDrivers/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
click_target = 5

for i in range(click_target):
    add_button.click()
    current_delete_buttons = driver.find_elements(By.CSS_SELECTOR, ".added-manually")

    assert len(current_delete_buttons) == i + 1

for i in range(click_target):
    delete_buttons = driver.find_elements(By.CSS_SELECTOR, ".added-manually")
    delete_buttons[0].click()
    remaining_buttons = driver.find_elements(By.CSS_SELECTOR, ".added-manually")
    expected_count = click_target - (i + 1)

    assert len(remaining_buttons) == expected_count
