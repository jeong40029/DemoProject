import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)

        checkoutpage = homepage.shopItems() #Shop button brings to checkoutpage
        log.info("Getting product cards")
        products = checkoutpage.GetCardPanels()
        for product in products:
            productName = checkoutpage.GetCardTitles(product).text
            log.info(productName)
            if productName == "Blackberry":
                checkoutpage.GetCardButtons(product).click()

        checkoutpage.GotoCheckoutPage().click()

        confirmpage = checkoutpage.CheckOutItems() #CheckOutIteams button brings to confirm page
        log.info("Entering Country name as 'Ind'")
        confirmpage.InputCountry().send_keys("Ind")

        self.verifyLinkPresence("India")

        confirmpage.SelectCountry().click()
        confirmpage.GetCheckbox().click()
        log.info("Submitting the order")
        confirmpage.Submit().click()
        alertMessage = confirmpage.GetAlertMessage().text
        log.info(alertMessage)

        assert "Success!" in alertMessage
