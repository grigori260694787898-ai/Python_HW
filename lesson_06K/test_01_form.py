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

        # 5. ПРОВЕРКА РЕЗУЛЬТАТА
        page_text = driver.page_source

        assert "Иван" in page_text, "Не найдено имя 'Иван' на странице результата"
        assert "Петров" in page_text, "Не найдена фамилия 'Петров' на странице результата"

        unexpected_value = "123456"
        if unexpected_value in page_text:
            raise AssertionError(
                f"Тест провален: на странице присутствует значение '{unexpected_value}', которого не вводили."
            )

        print("✅ Тест пройден: форма отправлена с пустым ZIP, поведение страницы зафиксировано.")

    except Exception as e:
        driver.save_screenshot("debug_screenshot.png")
        raise
    finally:
        driver.quit()
