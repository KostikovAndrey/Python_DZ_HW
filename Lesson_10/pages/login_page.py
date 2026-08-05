"""
Модуль с классом страницы логина.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Класс для работы со страницей логина.

    Attributes:
        USERNAME_INPUT (tuple): Локатор поля ввода имени пользователя.
        PASSWORD_INPUT (tuple): Локатор поля ввода пароля.
        LOGIN_BUTTON (tuple): Локатор кнопки входа.
        browser (WebDriver): Экземпляр браузера.
        wait (WebDriverWait): Объект для ожидания элементов.
    """
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, browser):
        """
        Инициализация страницы логина.

        Args:
            browser (WebDriver): Экземпляр браузера.
        """
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def open(self, url: str) -> None:
        """
        Открывает указанный URL в браузере.

        Args:
            url (str): URL страницы для открытия.

        Returns:
            None
        """
        self.browser.get(url)

    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему с указанными учетными данными.

        Args:
            username (str): Имя пользователя.
            password (str): Пароль.

        Returns:
            None
        """
        username_input = self.wait.until(
            EC.presence_of_element_located(self.USERNAME_INPUT)
        )
        username_input.send_keys(username)

        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)

        login_button = self.browser.find_element(*self.LOGIN_BUTTON)
        login_button.click()
