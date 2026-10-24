from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 90)

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    print("[INFO] Страница загружена")

    delay_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay")))
    delay_input.clear()
    delay_input.send_keys("45")
    print("[INFO] Введена задержка: 45 сек")

    buttons_to_click = ["7", "+", "8", "="]
    for text in buttons_to_click:
        btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[normalize-space()='{text}']")))
        btn.click()
        print(f"[INFO] Нажата кнопка: '{text}'")

    def result_is_15(d):
        html = d.page_source
        if "15" in html:
            print("[DEBUG] Текст '15' найден в HTML страницы!")
            return True
        return False

    wait.until(result_is_15)
    print("[✅] Результат «15» найден на странице!")

finally:
    # driver.quit()  # Раскомментируй, когда будешь уверен, что тест стабильно проходит
    pass
