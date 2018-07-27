import unittest
from selenium import webdriver
from selenium_tests.locators import Locators
from selenium_tests.wait import DriverWaits
from nose.plugins.attrib import attr
from selenium_tests.helpers import User


class TestSuit(unittest.TestCase):
    base_url = 'https://letskodeit.teachable.com/courses'
    username = 'test@email.com'
    password = 'abcabc'
    user = User(username, password)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver_waits = DriverWaits(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get(self.base_url)

    def tearDown(self):
        self.user.logout(self.driver)

    @attr("url_test")
    def test_current_url(self):
        """
        Test correct url is loaded
        :return:
        """
        current_url = self.driver.current_url
        error_msg = 'Current URL is wrong. Expected URL: {}; Actual URL: {}'.format(
            self.base_url, current_url
        )
        assert current_url == self.base_url, error_msg

    @attr("assignment_test")
    def test_login(self):

        self.user.login(self.driver, self.driver_waits)

        try:
            self.driver_waits.wait_till_text_is_present(Locators.MY_COURSES_LINK, "My Courses")
        except TimeoutError:
            raise AssertionError('Could not log in')

        user_image = self.driver.find_element(*Locators.USER_IMAGE)

        assert self.username == user_image.get_attribute('alt'), "user name is wrong"

    @attr("assignment_test")
    def test_for_selenium_course(self):
        self.user.login(self.driver, self.driver_waits)

        course_search_box = self.driver.find_element(*Locators.COURSE_SEARCH_INPUT_BOX)
        course_search_button = self.driver.find_element(*Locators.COURSE_SEARCH_INPUT_BUTTON)
        course_search_box.clear()

        course_to_search = "Selenium"

        course_search_box.send_keys(course_to_search)

        course_search_button.click()

        try:
            self.driver_waits.wait_till_button_is_clickable(Locators.COURSE_SEARCH_INPUT_BUTTON)
        except TimeoutError:
            raise AssertionError('Could not get to search results page')

        course_titles = self.driver.find_elements(*Locators.COURSE_TITLES)
        course_prices = self.driver.find_elements(*Locators.COURSE_PRICES)

        for course_title, course_price in zip(course_titles, course_prices):
            assert course_to_search in course_title.text, "{} is not a Selenium course".format(course_title.text)
            print(course_title.text, course_price.text)





