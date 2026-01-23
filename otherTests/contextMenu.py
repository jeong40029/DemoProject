from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/haydenjeong/WebDrivers/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/context_menu")
actions = ActionChains(driver)
clickBox = driver.find_element(By.CSS_SELECTOR, "#hot-spot")

actions.context_click(clickBox).perform()

alert = driver.switch_to.alert
print(alert.text)
alert.accept()

driver.quit()