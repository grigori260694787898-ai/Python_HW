from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_navigation():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://httpbin.qa-territory.online")

        # Находим ссылку по атрибуту href
        link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/forms/post"]'))
        )
        link.click()

        # Ждём, пока URL изменится на нужный
        wait.until(lambda d: d.current_url.endswith("/forms/post"))

        # Проверяем, что мы на странице /forms/post
        assert "/forms/post" in driver.current_url, f"Ожидался URL с /forms/post, но получен: {driver.current_url}"

        # Возвращаемся назад
        driver.back()

        # После возврата назад URL уже НЕ должен содержать /forms/post
        assert not "/forms/post" in driver.current_url, f"После back URL всё ещё содержит /forms/post: {driver.current_url}"

    finally:
        driver.quit()

if __name__ == "__main__":
    test_navigation()
