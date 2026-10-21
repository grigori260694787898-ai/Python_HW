from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 15)

try:
    
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay")))
    delay_input.clear()
    delay_input.send_keys("5")

    for text in ["7", "+", "8", "="]:
        btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[normalize-space()='{text}']")))
        btn.click()

    result_el = wait.until(EC.visibility_of_element_located((By.ID, "result")))

    def is_15(d):
        el = d.find_element(By.ID, "result")
        val = el.get_attribute("value") or el.text
        return (val or "").strip() == "15"

    wait.until(is_15)
    
finally:
    driver.quit()