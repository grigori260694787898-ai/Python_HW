from selenium import webdriver
from selenium.webdriver.common.by import By

def test_navigation():
    driver = webdriver.Chrome()
    driver.get(' https://httpbin.qa-territory.online')

    element = driver.find_element(By.CSS_SELECTOR, href="/forms/post")
    driver.current_url ("https://httpbin.qa-territory.online/forms/post")
    driver.back()
    driver.current_url ("https://httpbin.qa-territory.online")

    driver.quit()
