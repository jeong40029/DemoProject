from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    cardPanels = (By.XPATH, "//div[@class='card h-100']")
    cardTitles = (By.XPATH, "div/h4")
    cardButtons = (By.XPATH, "div/button")
    checkOut = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    itemsCheckOut = (By.CSS_SELECTOR, ".btn-success")

    def GetCardPanels(self):
        return self.driver.find_elements(*CheckoutPage.cardPanels)

    def GetCardTitles(self, products):
        return products.find_element(*CheckoutPage.cardTitles)

    def GetCardButtons(self, products):
        return products.find_element(*CheckoutPage.cardButtons)

    def GotoCheckoutPage(self):
        return self.driver.find_element(*CheckoutPage.checkOut)

    def CheckOutItems(self):
        self.driver.find_element(*CheckoutPage.itemsCheckOut).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage