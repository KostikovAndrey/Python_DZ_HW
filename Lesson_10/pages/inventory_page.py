"""
Модуль с классом страницы инвентаря.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """
    Класс для работы со страницей инвентаря.

    Attributes:
        CART_LINK (tuple): Локатор ссылки на корзину.
        browser (WebDriver): Экземпляр браузера.
        wait (WebDriverWait): Объект для ожидания элементов.
    """
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, browser):
        """
        Инициализация страницы инвентаря.

        Args:
            browser (WebDriver): Экземпляр браузера.
        """
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def add_item_to_cart(self, item_name: str) -> None:
        """
        Добавляет товар в корзину по его названию.

        Args:
            item_name (str): Название товара.

        Returns:
            None
        """
        item_xpath = (
            f"//div[text()='{item_name}']/ancestor::"
            f"div[@class='inventory_item']//button"
        )
        add_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, item_xpath))
        )
        add_button.click()

    def add_items_to_cart(self, items: list) -> None:
        """
        Добавляет несколько товаров в корзину.

        Args:
            items (list): Список названий товаров.

        Returns:
            None
        """
        for item in items:
            self.add_item_to_cart(item)

    def go_to_cart(self) -> None:
        """
        Переходит в корзину.

        Returns:
            None
        """
        cart_link = self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        )
        cart_link.click()
