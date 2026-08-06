"""
Тесты для интернет-магазина SauceDemo.
"""
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    """Фикстура для создания и закрытия драйвера Firefox."""
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.epic("Интернет-магазин")
@allure.feature("Оформление заказа")
@allure.story("Покупка товаров")
@allure.title("Тест оформления заказа в интернет-магазине")
@allure.description("Тест проверяет полный сценарий"
                    " покупки товаров в SauceDemo")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    """
    Тест проверяет полный сценарий покупки товаров:
    1. Авторизация
    2. Добавление товаров в корзину
    3. Оформление заказа
    4. Проверка итоговой суммы
    """
    with allure.step("Открытие страницы логина и авторизация"):
        login_page = LoginPage(driver)
        login_page.open("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        inventory_page = InventoryPage(driver)
        items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]
        inventory_page.add_items_to_cart(items)

    with allure.step("Переход в корзину"):
        inventory_page.go_to_cart()

    with allure.step("Переход к оформлению заказа"):
        cart_page = CartPage(driver)
        cart_page.proceed_to_checkout()

    with allure.step("Заполнение формы оформления заказа"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Иван", "Петров", "123456")

    with allure.step("Проверка итоговой суммы заказа"):
        total = checkout_page.get_total()
        expected_total = "Total: $58.29"
        assert total == expected_total, (
            f"Итоговая сумма {total}, ожидалось {expected_total}"
        )
