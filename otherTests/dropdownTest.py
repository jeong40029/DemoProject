from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/Users/haydenjeong/WebDrivers/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
actions = ActionChains(driver)

driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = driver.find_element(By.CSS_SELECTOR, "#dropdown")
select = Select(dropdown)
options = select.options

for option in options:
    print(option.text)

target_text = "Option 2"
select.select_by_visible_text(target_text)

current_text = select.first_selected_option.text
print(f"correct {target_text} is selected for {current_text}")
assert current_text == target_text, f"current selected text is {current_text} and expected is {target_text}"