from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_multiple_elements():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://httpbin.qa-territory.online/links/10")

        links = wait.until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
        )

        assert len(links) > 0, "Не найдено ни одной ссылки на странице"

        link_with_1 = next((l for l in links if "1" in l.text), None)
        assert link_with_1 is not None, "Не найдена ссылка, содержащая '1' в тексте"

        for i, link in enumerate(links):
            # Если ссылок много, можно ограничить проверку: if i >= 5: break
            assert link.is_displayed(), f"Ссылка №{i} не отображается: {link.text}"

    finally:
        driver.quit()

if __name__ == "__main__":
    test_multiple_elements()
