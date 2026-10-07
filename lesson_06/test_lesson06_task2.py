from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()


    driver.quit()

''' Подсказки
используйте методы для работы с cookie (добавление и очистка);
обновление страницы после установки cookie;
переход по URL профилей пользователей;
сохранение текущих URL для сравнения;
assert для проверки различий в URL.