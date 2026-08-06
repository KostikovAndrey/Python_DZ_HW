# Автотесты для интернет-магазина и калькулятора

## Описание проекта
Проект содержит автоматические тесты для:
- Интернет-магазина [SauceDemo](https://www.saucedemo.com/)
- Калькулятора с задержкой [Slow Calculator](https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html)

## Структура проекта
Lesson_10/
├── pages/
│ ├── init.py
│ ├── login_page.py
│ ├── inventory_page.py
│ ├── cart_page.py
│ └── checkout_page.py
├── calculator_page.py
├── test_shop.py
├── test_calculator.py
└── README.md


## Требования
- Python 3.8+
- Selenium
- pytest
- allure-pytest
- webdriver-manager

## Установка зависимостей
`bash
#pip install selenium pytest allure-pytest webdriver-manager flake8

## Установка Allure
scoop install allure

## Запуск тестов и формирование отчета
1. Запуск тестов с сохранением результатов
bash
pytest Lesson_10/ --alluredir=allure-results
2. Генерация отчета
bash
allure generate allure-results -o allure-report --clean
3. Просмотр отчета
bash
allure open allure-report
4. Полная команда (запуск + отчет)
bash
pytest Lesson_10/ --alluredir=allure-results && allure generate allure-results -o allure-report --clean && allure open allure-report
Проверка стиля кода (PEP8)
bash
flake8 Lesson_10/

## Описание тестов
test_shop.py - Тест интернет-магазина
Проверяет полный сценарий покупки: авторизация, добавление трех товаров в корзину, оформление заказа, проверка итоговой суммы. Ожидаемый результат: Total: $58.29

test_calculator.py - Тест калькулятора
Проверяет работу калькулятора с задержкой: установка задержки 45 секунд, ввод выражения 7+8=, ожидание результата 15.
