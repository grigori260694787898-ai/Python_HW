from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')

        start_btn = driver.find_element(By.CSS_SELECTOR, "#start > button")
        start_btn.click()

        # Ждём, пока в элементе с id="finish" появится текст "Hello World!"
        wait.until(
            EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!")
        )

        # Сохраняем скриншот
        driver.save_screenshot("hello_world_loaded.png")

        # Проверяем текст в элементе (реальный, а не придуманный)
        message_element = driver.find_element(By.ID, "finish")
        assert "Hello World!" in message_element.text, "Сообщение 'Hello World!' не появилось"

    finally:
        # Гарантированно закрываем браузер
        driver.quit()

if __name__ == "__main__":
    test_dynamic_loading()
