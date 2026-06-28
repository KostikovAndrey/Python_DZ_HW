from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()

    try:
        user1_cookie = {
            'name': 'SESSION',
            'value': 'YmZjNDM2OTQtYzdlMS00M2VlLWEyMWYtYjU2YjQ0ZDFlYTZh',
            'domain': '.gitflic.ru',
            'path': '/'
        }

        user2_cookie = {
            'name': 'SESSION',
            'value': 'ZTBlZjJiYzEtYTRhMi00MGI1LWE2MGYtYzg0NDZiY2E2ZjU4',
            'domain': '.gitflic.ru',
            'path': '/'
        }

        driver.get("https://gitflic.ru/")

        driver.add_cookie(user1_cookie)

        driver.refresh()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        driver.get("https://gitflic.ru/user/KostikovAM")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        url_user1 = driver.current_url
        print(f"URL пользователя 1 (KostikovAM): {url_user1}")

        driver.delete_all_cookies()

        driver.add_cookie(user2_cookie)

        driver.refresh()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        driver.get("https://gitflic.ru/user/Kasiposha")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        url_user2 = driver.current_url
        print(f"URL пользователя 2 (Kasiposha): {url_user2}")

        assert url_user1 != url_user2, (
            f"URLs should be different for different users. "
            f"URL1: {url_user1}, URL2: {url_user2}"
        )

        print("✅ Тест успешно пройден! URL разных пользователей различаются!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_session_storage_auth()
