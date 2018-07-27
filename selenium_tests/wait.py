from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_tests.locators import Locators


class DriverWaits(object):

    def __init__(self, driver, timeout=10, poll_frequency=1):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency)

    def wait_till_text_is_present(self, locator, text):
        self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def wait_till_button_is_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))