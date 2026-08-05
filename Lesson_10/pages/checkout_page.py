"""
Модуль с классом страницы оформления заказа.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Класс для работы со страницей оформления заказа.

    Attributes:
        FIRST_NAME_INPUT (tuple): Локатор поля ввода имени.
        LAST_NAME_INPUT (tuple): Локатор поля ввода фамилии.
        POSTAL_CODE_INPUT (tuple): Локатор поля ввода почтового индекса.
        CONTINUE_BUTTON (tuple): Локатор кнопки продолжения.
        TOTAL_LABEL (tuple): Локатор элемента с итоговой суммой.
        browser (WebDriver): Экземпляр браузера.
        wait (WebDriverWait): Объект для ожидания элементов.
    """
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, browser):
        """
        Инициализация страницы оформления заказа.

        Args:
            browser (WebDriver): Экземпляр браузера.
        """
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def fill_form(self, first_name: str, last_name: str,
                  postal_code: str) -> None:
        """
        Заполняет форму оформления заказа.

        Args:
            first_name (str): Имя.
            last_name (str): Фамилия.
            postal_code (str): Почтовый индекс.

        Returns:
            None
        """
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

    def get_total(self) -> str:
        """
        Получает итоговую сумму заказа.

        Returns:
            str: Текст с итоговой суммой.
        """
        total_element = self.wait.until(
            EC.presence_of_element_located(self.TOTAL_LABEL)
        )
        return total_element.text
