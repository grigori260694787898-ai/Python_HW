from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
import os


def wait_for_page_load(driver, timeout=30):
    """Ждёт полной загрузки страницы (document.readyState == 'complete')"""
    wait_local = WebDriverWait(driver, timeout)
    wait_local.until(lambda d: d.execute_script("return document.readyState") == "complete")


def get_element_css_classes(element):
    """Возвращает список классов элемента для проверки подсветки/валидации"""
    return element.get_attribute("class").split() if element.get_attribute("class") else []


def has_validation_class(element, invalid_classes=None):
    """Проверяет, есть ли у элемента класс, означающий ошибку валидации"""
    if invalid_classes is None:
        # Подставь сюда те классы, которые реально использует страница для ошибок
        invalid_classes = ["error", "invalid", "is-invalid", "has-error"]
    classes = get_element_css_classes(element)
    return any(c in classes for c in invalid_classes)


def test_form_submission_with_empty_zip():
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    wait = WebDriverWait(driver, 30)

    try:
        # 1. Открываем страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        wait_for_page_load(driver)

        # 2. Заполняем все поля, КРОМЕ zip-code
        fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+79858999987",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        for name, val in fields.items():
            el = wait.until(EC.visibility_of_element_located((By.NAME, name)))
            el.clear()
            el.send_keys(val)

        # 3. Находим поле ZIP и оставляем его ПУСТЫМ
        zip_el = wait.until(EC.visibility_of_element_located((By.NAME, "zip-code")))
        zip_el.clear()
        # Убедимся, что поле действительно пустое
        assert zip_el.get_attribute("value") == "", "Поле zip-code не пустое после clear()"

        # 4. Нажимаем Submit
        submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        submit_btn.click()

        # Сохраняем скриншот сразу после клика (для отладки)
        driver.save_screenshot("after_submit_click.png")

        # Ждём загрузки страницы результата
        wait_for_page_load(driver)

        # Сохраняем финальный скриншот
        driver.save_screenshot("after_page_load.png")
        print(f"[INFO] Скриншоты сохранены. Путь: {os.getcwd()}")

        # --- ПРОВЕРКИ ЗНАЧЕНИЙ (каждое поле отдельно) ---
        page_text = driver.page_source

        for field_name, expected_value in fields.items():
            assert expected_value in page_text, f"Не найдено значение '{expected_value}' для поля '{field_name}'"

        # Проверка, что ZIP остался пустым (не подставилось никакое дефолтное значение)
        unexpected_value = "123456"
        if unexpected_value in page_text:
            raise AssertionError(
                f"Тест провален: на странице присутствует значение '{unexpected_value}', которого не вводили."
            )

        # --- ПРОВЕРКИ ПОДСВЕТКИ (валидации) ---
        # Если страница после сабмита подсвечивает ошибочные поля — проверяем это.
        # Важно: подставь реальные классы валидации, которые использует сайт.
        error_classes = ["error", "invalid", "is-invalid", "has-error"]  # можно расширить

        # Для заполненных полей ожидаем, что они НЕ подсвечены как ошибки
        for name in fields:
            el = driver.find_element(By.NAME, name)
            assert not has_validation_class(el, error_classes), f"Поле '{name}' подсвечено как ошибка, хотя заполнено корректно"

        # Для поля ZIP: отдельная логика
        # Вариант А: если пустое ZIP — это ошибка, то у него должен быть класс ошибки
        # Раскомментируй эту строку, если на странице пустое ZIP подсвечивается как ошибка:
        # assert has_validation_class(zip_el, error_classes), "Поле zip-code должно быть подсвечено как ошибка (оно пустое)"

        # Вариант Б: если пустое ZIP — допустимо, то оно НЕ должно быть подсвечено ошибкой
        assert not has_validation_class(zip_el, error_classes), "Поле zip-code подсвечено как ошибка, но пустое значение разрешено"

        print("✅ Тест пройден: все поля проверены по значению и подсветке.")

    except Exception as e:
        driver.save_screenshot("debug_screenshot.png")
        raise
    finally:
        driver.quit()
