from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    link_text = link.text

assert "1" in links[0].text

for link in links:    
    assert link.is_displayed()

driver.quit()
