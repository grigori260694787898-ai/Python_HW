from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import re

# Настройка Firefox
options = Options()
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
wait = WebDriverWait(driver, 90)

try:
    # 1. Открыть сайт магазина
    driver.get("https://www.saucedemo.com/")
    print("[INFO] Сайт открыт")

    # 2. Авторизация
    username_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    password_input = driver.find_element(By.ID, "password")
    
    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    
    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()
    print("[INFO] Авторизация выполнена")

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

    # 3. Добавить товары в корзину
    products_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for product_name in products_to_add:
        product_card = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//div[contains(@class, 'inventory_item') and .//div[text()='{product_name}']]")
            )
        )
        add_btn = product_card.find_element(By.CSS_SELECTOR, ".btn_primary.btn_inventory")
        add_btn.click()
        print(f"[INFO] В корзину добавлен: {product_name}")

    # 4. Перейти в корзину и нажать Checkout
    cart_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shopping_cart_container a")))
    cart_link.click()
    print("[INFO] Переход в корзину выполнен")

    checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_btn.click()
    print("[INFO] Нажата кнопка Checkout")

    # 5. Заполнить форму своими данными
    first_name_input = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
    last_name_input = driver.find_element(By.ID, "last-name")
    postal_code_input = driver.find_element(By.ID, "postal-code")

    first_name_input.send_keys("Ivan")
    last_name_input.send_keys("Petrov")
    postal_code_input.send_keys("12345")
    print("[INFO] Форма заполнена")

    continue_btn = driver.find_element(By.ID, "continue")
    continue_btn.click()
    print("[INFO] Нажата кнопка Continue")

    # 6. Прочитать итоговую стоимость и проверить, что она равна $58.29
    total_el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
    total_text = total_el.text.strip()
    print(f"[DEBUG] Текст итоговой стоимости: '{total_text}'")

    expected_total = 58.29

    match = re.search(r"\$(\d+\.\d{2})", total_text)
    if not match:
        raise AssertionError(f"Не удалось извлечь сумму из текста '{total_text}'. Ожидался формат 'Total: $XX.XX'")

    actual_total = float(match.group(1))
    assert actual_total == expected_total, f"Итоговая сумма не совпадает! Ожидалось ${expected_total}, но получено ${actual_total}"

    print("[✅] Итоговая сумма проверена и совпадает: $58.29")

finally:
    # 7. Закрыть браузер
    driver.quit()
    print("[INFO] Браузер закрыт")
