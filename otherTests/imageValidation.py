from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/haydenjeong/WebDrivers/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/broken_images")

broken_images_list = []
images = driver.find_elements(By.TAG_NAME, "img")
for img in images:
    is_valid = driver.execute_script(
        "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0",
        img
    )

    if not is_valid:
        src = img.get_attribute("src")
        broken_images_list.append(src)

print(broken_images_list)
assert len(broken_images_list) == 0
