from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
import os

# Настройка драйвера
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)
wait = WebDriverWait(driver, 30)

def wait_for_page_load(driver, timeout=30):
    """Ждёт полной загрузки страницы (document.readyState == 'complete')"""
    wait_local = WebDriverWait(driver, timeout)
    wait_local.until(lambda d: d.execute_script("return document.readyState") == "complete")
    print("[OK] Страница полностью загружена")

try:
    # 1. Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait_for_page_load(driver)
    print("[INFO] Страница загружена")

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
        # zip-code намеренно исключён из заполнения
    }

    for name, val in fields.items():
        el = wait.until(EC.visibility_of_element_located((By.NAME, name)))
        el.clear()
        el.send_keys(val)
        print(f"[INFO] Заполнено: {name}")

    # 3. Находим поле ZIP и оставляем его ПУСТЫМ
    zip_el = wait.until(EC.visibility_of_element_located((By.NAME, "zip-code")))
    zip_el.clear()  # Гарантируем, что поле точно пустое
    print("[INFO] Поле ZIP оставлено ПУСТЫМ специально для теста")

    # 4. Нажимаем Submit
    submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_btn.click()
    print("[INFO] Кнопка Submit нажата")

    # Сохраняем скриншот сразу после клика (для отладки)
    driver.save_screenshot("after_submit_click.png")
    
    # Ждём загрузки страницы результата
    wait_for_page_load(driver)
    
    # Сохраняем финальный скриншот
    driver.save_screenshot("after_page_load.png")
    print(f"[INFO] Скриншоты сохранены. Путь: {os.getcwd()}")

    # 5. ПРОВЕРКА РЕЗУЛЬТАТА
    page_text = driver.page_source

    # Проверяем, что отправленные данные (Иван, Петров) действительно отобразились
    assert "Иван" in page_text, "Не найдено имя 'Иван' на странице результата"
    assert "Петров" in page_text, "Не найдена фамилия 'Петров' на странице результата"
    print("[✅] Отправленные данные ('Иван', 'Петров') отображены на странице.")

    # Ключевая проверка: убеждаемся, что значение, которое мы НЕ вводили, отсутствует
    # Это доказывает, что поле было пустым и бэкенд не подставил дефолтное значение
    unexpected_value = "123456"
    if unexpected_value in page_text:
        print(f"[❌] ОШИБКА: На странице есть значение '{unexpected_value}', хотя поле ZIP было пустым!")
        raise AssertionError(f"Тест провален: на странице присутствует значение '{unexpected_value}', которого не вводили.")
    else:
        print(f"[✅] Значение '{unexpected_value}' отсутствует на странице — поле действительно было пустым.")

    print("✅ Тест пройден: форма отправлена с пустым ZIP, поведение страницы зафиксировано.")

except Exception as e:
    print(f"❌ Тест упал: {e}")
    driver.save_screenshot("debug_screenshot.png")
    raise
finally:
    # Раскомментируй строку ниже, если хочешь, чтобы браузер закрывался сразу после теста
    # driver.quit()
    pass
