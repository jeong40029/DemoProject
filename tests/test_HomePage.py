import pytest
from selenium.webdriver.support.select import Select

from TestData.HomepageData import HomepageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from selenium import webdriver

class TestHomePage(BaseClass):
    def test_formSubmissions(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("Firstname is "+getData["firstname"])
        homepage.enterName().send_keys(getData["firstname"])
        log.info("Email is "+getData["email"])
        homepage.enterEmail().send_keys(getData["email"])
        homepage.clickCheckbox().click()
        log.info("Gender is "+getData["gender"])
        self.selectOptionByText(homepage.getGender(), getData["gender"])

        log.info("Submitting the form...")
        homepage.clickSubmit().click()
        msg = homepage.getAlertMessage().text

        assert "Success!" in msg
        self.driver.refresh()

    @pytest.fixture(params=HomepageData.test_HomePage_Data)
    def getData(self, request):
        return request.param