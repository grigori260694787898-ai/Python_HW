from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
wait = WebDriverWait(driver, 90)  # 90 секунд на ожидание элементов

try:
    # 1. Открыть сайт
    driver.get("https://www.saucedemo.com/")
    
    username_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    password_input = driver.find_element(By.ID, "password")
    
    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
    
    products_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for product_name in products_to_add:
        # Ищем карточку по тексту названия
        product_card = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//div[contains(@class, 'inventory_item') and .//div[text()='{product_name}']]")
            )
        )
        add_btn = product_card.find_element(By.CSS_SELECTOR, ".btn_primary.btn_inventory")
        add_btn.click()
        
    
    cart_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shopping_cart_container a")))
    cart_link.click()

    
    checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_btn.click()

    
    first_name_input = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
    last_name_input = driver.find_element(By.ID, "last-name")
    postal_code_input = driver.find_element(By.ID, "postal-code")

    first_name_input.send_keys("Ivan")
    last_name_input.send_keys("Petrov")
    postal_code_input.send_keys("12345")

    continue_btn = driver.find_element(By.ID, "continue")
    continue_btn.click()

    total_el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
    total_text = total_el.text.strip()
   
finally:
    driver.quit()