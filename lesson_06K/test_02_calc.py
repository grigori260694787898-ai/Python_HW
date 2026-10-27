from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os


def wait_for_page_load(driver, timeout=90):
    """Ждёт полной загрузки страницы (document.readyState == 'complete')"""
    wait_local = WebDriverWait(driver, timeout)
    wait_local.until(lambda d: d.execute_script("return document.readyState") == "complete")


def test_slow_calculator_7_plus_8_equals_15():
    """Тест: 7 + 8 = 15 на slow-calculator с задержкой 45 сек, проверка результата и отсутствие ошибок"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 90)

    try:
        # 1. Открываем страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        wait_for_page_load(driver)
        print("[INFO] Страница загружена")

        # 2. Устанавливаем задержку 45 секунд
        delay_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()
        delay_input.send_keys("45")
        print("[INFO] Введена задержка: 45 сек")

        # Скриншот после ввода задержки (удобно для отладки)
        driver.save_screenshot("after_delay_input.png")

        # 3. Нажимаем кнопки: 7 + 8 =
        buttons_to_click = ["7", "+", "8", "="]
        for text in buttons_to_click:
            btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[normalize-space()='{text}']")))
            btn.click()
            print(f"[INFO] Нажата кнопка: '{text}'")

        # 4. Ждём появления результата «15»
        def result_is_15(d):
            html = d.page_source
            if "15" in html:
                print("[DEBUG] Текст '15' найден в HTML страницы!")
                return True
            return False

        wait.until(result_is_15)
        print("[✅] Результат «15» найден на странице!")

        # --- ASSERT-ПРОВЕРКИ ---

        # Проверка 1: результат действительно равен 15
        assert "15" in driver.page_source, "Ожидаемый результат '15' не найден на странице"

        # Проверка 2: убеждаемся, что нет ошибочных сообщений
        error_indicators = ["Error", "Timeout", "Failed", "error"]
        page_text = driver.page_source
        for err in error_indicators:
            assert err not in page_text, f"На странице найдено сообщение об ошибке: '{err}'"

        # Проверка 3 (опционально): убедимся, что выражение отображается (если страница его показывает)
        if any(expr in page_text for expr in ["7 + 8", "7+8"]):
            print("[INFO] Выражение '7 + 8' отображается на странице")

        # Финальный скриншот
        driver.save_screenshot("after_page_load.png")
        print(f"[INFO] Скриншоты сохранены. Путь: {os.getcwd()}")

        print("✅ Тест пройден: результат сложения 7 + 8 равен 15, ошибок не обнаружено.")

    except Exception as e:
        driver.save_screenshot("debug_screenshot.png")
        raise
    finally:
        driver.quit()
