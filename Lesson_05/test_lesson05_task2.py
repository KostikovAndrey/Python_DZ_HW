from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Иван Петров")

    submit_button = driver.find_element(
        By.XPATH, "//button[text()='Submit order']"
    )
    submit_button.click()

    current_url = driver.current_url
    expected_text = "/post"
    assert expected_text in current_url, (
        f"Ожидался URL с {expected_text}, получен: {current_url}"
    )
    print(f"URL после отправки: {current_url}")
    print("Тест успешно пройден!")

    driver.quit()
