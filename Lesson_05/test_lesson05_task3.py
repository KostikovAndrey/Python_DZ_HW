from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")

    all_links = driver.find_elements(By.TAG_NAME, "a")

    expected_count = 9
    actual_count = len(all_links)
    assert actual_count == expected_count, (
        f"Ожидалось {expected_count} ссылок, найдено {actual_count}"
    )
    print(f"Найдено {actual_count} ссылок")

    for i, link in enumerate(all_links):
        assert link.is_displayed(), (
            f"Ссылка с индексом {i} не отображается на странице"
        )
    print("Все ссылки отображаются")

    first_link_text = all_links[0].text
    assert "1" in first_link_text, (
        f"Текст первой ссылки '{first_link_text}' не содержит '1'"
    )
    print(f"Текст первой ссылки: '{first_link_text}', содержит '1'")

    print("Все проверки успешно пройдены!")

    driver.quit()
