from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_submission():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://httpbin.qa-territory.online/forms/post")

        name_field = wait.until(
            EC.element_to_be_clickable((By.NAME, "custname"))
        )
        name_field.send_keys("Григорий Бологов")

        submit_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit order']"))
        )
        submit_btn.click()

        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
        )

        success_indicator = wait.until(
            lambda d: "Order submitted" in d.page_source
        )
        assert success_indicator, "Не найден признак успешной отправки формы"

        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_form_submission()
