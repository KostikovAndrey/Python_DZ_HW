from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def fill_form(self, first_name, last_name, postal_code):
        first_name_input = self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        )
        first_name_input.send_keys(first_name)

        last_name_input = self.browser.find_element(*self.LAST_NAME_INPUT)
        last_name_input.send_keys(last_name)

        postal_code_input = self.browser.find_element(*self.POSTAL_CODE_INPUT)
        postal_code_input.send_keys(postal_code)

        continue_button = self.browser.find_element(*self.CONTINUE_BUTTON)
        continue_button.click()

    def get_total(self):
        total_element = self.wait.until(
            EC.presence_of_element_located(self.TOTAL_LABEL)
        )
        return total_element.text
