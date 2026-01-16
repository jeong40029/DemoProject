from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    countryInput = (By.CSS_SELECTOR, ".validate")
    countryLink = (By.LINK_TEXT, "India")
    countrySelect = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//label[@for='checkbox2']")
    submitButton = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
    alertMessage = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def InputCountry(self):
        return self.driver.find_element(*ConfirmPage.countryInput)

    def SelectCountry(self):
        return self.driver.find_element(*ConfirmPage.countrySelect)

    def GetCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def Submit(self):
        return self.driver.find_element(*ConfirmPage.submitButton)

    def GetAlertMessage(self):
        return self.driver.find_element(*ConfirmPage.alertMessage)