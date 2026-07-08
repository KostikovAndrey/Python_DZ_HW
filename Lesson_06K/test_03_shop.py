import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    username = wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item in items:
        item_xpath = (
            f"//div[text()='{item}']/ancestor::"
            f"div[@class='inventory_item']//button"
        )
        add_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, item_xpath))
        )
        add_button.click()

    cart = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    )
    cart.click()

    checkout = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout.click()

    first_name = wait.until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Петров")

    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("123456")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    total = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".summary_total_label")
        )
    )
    total_text = total.text

    assert total_text == "Total: $58.29", (
        f"Итоговая сумма {total_text}, ожидалось Total: $58.29"
    )
