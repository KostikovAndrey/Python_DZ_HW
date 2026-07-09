from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 45)

    def open(self, url):
        self.browser.get(url)

    def set_delay(self, seconds):
        delay_input = self.browser.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_button(self, value):
        xpath = f"//span[text()='{value}']"
        button = self.browser.find_element(By.XPATH, xpath)
        button.click()

    def click_buttons_sequence(self, buttons):
        for button in buttons:
            self.click_button(button)

    def wait_for_result(self, expected_value):
        return self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_value)
        )
