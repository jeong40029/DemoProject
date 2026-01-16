import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("/Users/haydenjeong/PycharmProjects/PythonSelFramework/utilities/test.log")
        formatter = logging.Formatter("%(asctime)s: %(name)s: %(levelname)s: %(message)s")
        logger.addHandler(filehandler)
        filehandler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)
        return logger