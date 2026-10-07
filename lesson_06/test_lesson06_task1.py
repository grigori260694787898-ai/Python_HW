from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2.')

    Start_btn = driver.find_element(By.CSS_SELECTOR, "#start > button")
    Start_btn.click()

    WebDriverWait(driver, 10).until(
     EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!")
 )

message = wait.until(
        EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!")
    )
# message_element = driver.find_element(By.ID, "finish")
#   assert message_element.text == "Hello World!", "Сообщение 'Hello World!' появилось"

save_screenshot()

text = "Hello World!"
assert text == "Hello World!", f"Текст совпал. Получено: {text}"

driver.quit()
