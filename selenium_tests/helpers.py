from selenium_tests.locators import Locators

class User:

    def __init__(self, username = "test@email.com", password = "abcabc"):
        self.user_name = username
        self.password = password

    def login(self, driver, driver_waits):
         login_link = driver.find_element(*Locators.LOGIN_LINK)
         login_link.click()

         try:
             driver_waits.wait_till_text_is_present(Locators.LOGIN_PAGE_HEADER, "Log In to Let's Kode It")
         except TimeoutError:
             raise AssertionError('Could not access log in page')

         login_email_input = driver.find_element(*Locators.LOGIN_EMAIL)
         login_password_input = driver.find_element(*Locators.LOGIN_PASSWORD)

         login_email_input.clear()
         login_password_input.clear()

         login_email_input.send_keys(self.user_name)
         login_password_input.send_keys(self.password)

         login_button = driver.find_element(*Locators.LOGIN_BUTTON)
         login_button.click()

    def logout(self, driver):
        user_image = driver.find_element(*Locators.USER_IMAGE)
        user_image.click()
        logout_link = driver.find_element(*Locators.LOGOUT_LIST)
        logout_link.click()

