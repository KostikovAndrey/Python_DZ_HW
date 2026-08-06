"""
Тесты для калькулятора.
"""
import allure
import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def browser():
    """Фикстура для создания и закрытия драйвера Chrome."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.epic("Калькулятор")
@allure.feature("Вычисления")
@allure.story("Сложение с задержкой")
@allure.title("Тест калькулятора с задержкой")
@allure.description("Тест проверяет работу калькулятора с задержкой")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator(browser):
    """
    Тест проверяет работу калькулятора с задержкой:
    1. Открытие страницы калькулятора
    2. Установка задержки
    3. Ввод выражения 7+8=
    4. Проверка результата
    """
    with allure.step("Открытие страницы калькулятора"):
        calculator_page = CalculatorPage(browser)
        url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        calculator_page.open(url)

    with allure.step("Установка задержки 45 секунд"):
        calculator_page.set_delay("45")

    with allure.step("Ввод выражения 7+8="):
        buttons = ["7", "+", "8", "="]
        calculator_page.click_buttons_sequence(buttons)

    with allure.step("Проверка результата (ожидается 15)"):
        result = calculator_page.wait_for_result("15")
        assert result, "Результат не появился на экране калькулятора"
