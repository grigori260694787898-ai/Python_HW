from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2.')
    button = driver.find_element(By.CSS_SELECTOR, "#start > button")
    button.click()

    WebDriverWait(driver, 10).until(
     EC.text_to_be_present_in_element((By.ID, "id="finish""), "Hello World!")
 )
    save_screenshot()

    text = "Hello World!"
assert text == "Hello World!", f"Текст совпал. Получено: {text}"

    driver.quit()
