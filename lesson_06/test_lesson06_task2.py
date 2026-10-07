
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")

driver.add_cookie({
    "name": "SESSION",
    "vaule": "ZTRlMjMzYzctNzM4Ni00OGUzLTkwMmItNWE2NDU1ZWVhM2Mz",
    "domain": "gitflic.ru"
})

driver.get("https://gitflic.ru/user/grigori260694")
url_user1 = driver1.current_url

driver.refresh() 

driver.delete_all_cookies()

driver.get("https://gitflic.ru/")
driver.add_cookie({
    "name": "SESSION",
    "vaule": "YmJkZDkzZTctMzg1NS00ZGIwLWFjYmUtMTFhYWI0ZjNmNWMy",
    "domain": "gitflic.ru"
})

driver.get("https://gitflic.ru/user/greg260694")
url_user2 = driver1.current_url

driver.refresh() 

driver.delete_all_cookies()

assert url_user1 != url_user2, f"Ошибка: URL различаются!"

driver.quit()
