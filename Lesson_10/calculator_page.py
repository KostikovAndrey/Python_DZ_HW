"""
Модуль с классом страницы калькулятора.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Класс для работы со страницей калькулятора.

    Attributes:
        DELAY_INPUT (tuple): Локатор поля ввода задержки.
        SCREEN (tuple): Локатор экрана калькулятора.
        browser (WebDriver): Экземпляр браузера.
        wait (WebDriverWait): Объект для ожидания элементов.
    """
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, browser):
        """
        Инициализация страницы калькулятора.

        Args:
            browser (WebDriver): Экземпляр браузера.
        """
        self.browser = browser
        self.wait = WebDriverWait(browser, 45)

    def open(self, url: str) -> None:
        """
        Открывает указанный URL в браузере.

        Args:
            url (str): URL страницы для открытия.

        Returns:
            None
        """
        self.browser.get(url)

    def set_delay(self, seconds: str) -> None:
        """
        Устанавливает задержку в калькуляторе.

        Args:
            seconds (str): Количество секунд задержки.

        Returns:
            None
        """
        delay_input = self.browser.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_button(self, value: str) -> None:
        """
        Нажимает кнопку на калькуляторе.

        Args:
            value (str): Значение кнопки.

        Returns:
            None
        """
        xpath = f"//span[text()='{value}']"
        button = self.browser.find_element(By.XPATH, xpath)
        button.click()

    def click_buttons_sequence(self, buttons: list) -> None:
        """
        Нажимает последовательность кнопок на калькуляторе.

        Args:
            buttons (list): Список значений кнопок.

        Returns:
            None
        """
        for button in buttons:
            self.click_button(button)

    def wait_for_result(self, expected_value: str) -> bool:
        """
        Ожидает появления ожидаемого результата на экране калькулятора.

        Args:
            expected_value (str): Ожидаемое значение.

        Returns:
            bool: True если результат появился.
        """
        return self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_value)
        )
