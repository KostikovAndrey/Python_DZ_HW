from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.org/")
    original_url = driver.current_url
    print(f"Начальный URL: {original_url}")

    html_form_link = driver.find_element(By.LINK_TEXT, "HTML form")
    html_form_link.click()

    current_url = driver.current_url
    expected_text = "/forms/post"
    assert expected_text in current_url, (
        f"Ожидался URL с {expected_text}, получен: {current_url}"
    )
    print(f"URL после клика: {current_url}")

    driver.back()

    current_url = driver.current_url
    assert current_url == original_url, (
        f"Ожидался URL {original_url}, получен: {current_url}"
    )
    print(f"Вернулись на исходный URL: {current_url}")

    print("Тест успешно пройден!")

    driver.quit()
