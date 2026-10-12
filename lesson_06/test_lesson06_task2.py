from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Первый сеанс
        driver.get("https://gitflic.ru/")
        driver.add_cookie({
            "name": "SESSION",
            "value": "TEST_SESSION_VALUE_1",
            "domain": "gitflic.ru",
            "path": "/"
        })
        driver.refresh()
        wait.until(lambda d: d.current_url != "")  
        url_user1 = driver.current_url

        # Второй сеанс
        driver.delete_all_cookies()
        driver.get("https://gitflic.ru/")
        driver.add_cookie({
            "name": "SESSION",
            "value": "TEST_SESSION_VALUE_2",
            "domain": "gitflic.ru",
            "path": "/"
        })
        driver.refresh()
        wait.until(lambda d: d.current_url != "")
        url_user2 = driver.current_url

        assert url_user1 != url_user2, f"URL должны различаться: {url_user1} vs {url_user2}"

    finally:
        driver.quit()

if __name__ == "__main__":
    test_session_storage_auth()
