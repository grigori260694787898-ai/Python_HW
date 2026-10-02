from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    link_text = link.text

links = driver.find_elements(By.TAG_NAME, "a")

if links and "1" in links[0].text:
    print("Текст первой ссылки содержит '1'")
else:
    print("Ссылка не найдена или не содержит '1'")

driver.quit()
