from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def open(self, url):
        self.browser.get(url)

    def login(self, username, password):
        username_input = self.wait.until(
            EC.presence_of_element_located(self.USERNAME_INPUT)
        )
        username_input.send_keys(username)

        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)

        login_button = self.browser.find_element(*self.LOGIN_BUTTON)
        login_button.click()
