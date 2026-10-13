from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Селектор элемента, который точно есть на странице профиля
# Если не сработает — подберём по реальному HTML
PROFILE_INDICATOR = (By.CSS_SELECTOR, "h1, .user-name, .profile-header")

def run_session(session_value, profile_url, output_file):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # раскомментируй, если не нужно окно браузера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 15)

    try:
        # Сначала заходим на домен, чтобы браузер «принял» куки для этого домена
        driver.get("https://gitflic.ru/")

        # Добавляем сессию
        driver.add_cookie({
            "name": "SESSION",
            "value": session_value,
            "domain": "gitflic.ru",
            "path": "/"
        })

        # Обновляем страницу, чтобы сессия применилась
        driver.refresh()

        # Переход на профиль
        driver.get(profile_url)

        # Ждём загрузки профиля
        wait.until(EC.presence_of_element_located(PROFILE_INDICATOR))

        final_url = driver.current_url
        print(f"Переход выполнен. URL: {final_url}")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(final_url)
        print(f"URL сохранён в {output_file}")

        return final_url

    except Exception as e:
        print(f"Ошибка в сессии {session_value}: {e}")
        raise
    finally:
        driver.quit()


def test_session_storage_auth():
    url_user1 = run_session("TEST_SESSION_VALUE_1", "https://gitflic.ru/user/grigori260694", "user1_profile_url.txt")
    url_user2 = run_session("TEST_SESSION_VALUE_2", "https://gitflic.ru/user/greg260694", "user2_profile_url.txt")

    assert url_user1 != url_user2, f"URL должны различаться: {url_user1} vs {url_user2}"
    print("Проверка пройдена: URL различаются.")


if __name__ == "__main__":
    test_session_storage_auth()
