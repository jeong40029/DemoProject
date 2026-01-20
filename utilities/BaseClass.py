import inspect
import logging
import os

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

        current_dir = os.path.dirname(os.path.abspath(__file__))
        log_file_path = os.path.join(current_dir, "test.log")

        filehandler = logging.FileHandler(log_file_path)

        formatter = logging.Formatter("%(asctime)s: %(name)s: %(levelname)s: %(message)s")
        filehandler.setFormatter(formatter)

        if not logger.handlers:
            logger.addHandler(filehandler)
            logger.setLevel(logging.INFO)

        return logger