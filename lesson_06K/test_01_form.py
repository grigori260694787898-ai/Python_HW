from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

# Инициализация драйвера через webdriver-manager
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

# Создаём объект ожидания
wait = WebDriverWait(driver, 15)  # увеличил таймаут для стабильности

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполняем поля
    wait.until(EC.visibility_of_element_located((By.NAME, "first-name"))).send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

    other_fields = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    print("Все проверки пройдены!")

finally:
    driver.quit()