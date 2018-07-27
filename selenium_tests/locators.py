from selenium.webdriver.common.by import By

class Locators:
    LOGIN_LINK = (By.CSS_SELECTOR, "a.navbar-link.fedora-navbar-link[href='/sign_in']")
    LOGIN_PAGE_HEADER = (By.CSS_SELECTOR, "h1.text-center")
    LOGIN_EMAIL = (By.ID, "user_email")
    LOGIN_PASSWORD = (By.ID, "user_password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login-button")
    MY_COURSES_LINK = (By.CSS_SELECTOR, ".fedora-navbar-link.navbar-link[href='/courses/enrolled']")
    USER_IMAGE = (By.CSS_SELECTOR, ".gravatar[alt='test@email.com']")
    COURSE_SEARCH_INPUT_BOX = (By.ID, "search-courses")
    COURSE_SEARCH_INPUT_BUTTON = (By.ID, "search-course-button")
    COURSE_TITLES = (By.CLASS_NAME, "course-listing-title")
    COURSE_PRICES = (By.CLASS_NAME, "course-price")
    LOGOUT_LIST = (By.CSS_SELECTOR, ".user-signout")
