import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(browser):
    calculator_page = CalculatorPage(browser)

    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    calculator_page.open(url)

    calculator_page.set_delay("45")

    buttons = ["7", "+", "8", "="]
    calculator_page.click_buttons_sequence(buttons)

    result = calculator_page.wait_for_result("15")
    assert result
