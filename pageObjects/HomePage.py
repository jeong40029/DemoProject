from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[text()='Shop']")
    name = (By.XPATH, "//input[@name='name']")
    email = (By.XPATH, "//input[@name='email']")
    checkbox = (By.CSS_SELECTOR, "#exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.CSS_SELECTOR, ".btn-success")
    alert = (By.CSS_SELECTOR, ".alert")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage

    def enterName(self):
        return self.driver.find_element(*HomePage.name)

    def enterEmail(self):
        return self.driver.find_element(*HomePage.email)

    def clickCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def clickSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getAlertMessage(self):
        return self.driver.find_element(*HomePage.alert)