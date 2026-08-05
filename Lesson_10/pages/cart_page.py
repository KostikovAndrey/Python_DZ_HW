"""
Модуль с классом страницы корзины.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Класс для работы со страницей корзины.

    Attributes:
        CHECKOUT_BUTTON (tuple): Локатор кнопки оформления заказа.
        browser (WebDriver): Экземпляр браузера.
        wait (WebDriverWait): Объект для ожидания элементов.
    """
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, browser):
        """
        Инициализация страницы корзины.

        Args:
            browser (WebDriver): Экземпляр браузера.
        """
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def proceed_to_checkout(self) -> None:
        """
        Переходит к оформлению заказа.

        Returns:
            None
        """
        checkout_button = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_button.click()
