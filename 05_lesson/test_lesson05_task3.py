from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    # 1. Находим все ссылки на странице
    links = driver.find_elements(By.TAG_NAME, "a")

    # 2. Проверяем, что количество ссылок равно 9
    assert len(links) == 9

    # 3. Проверяем, что все ссылки отображаются
    for link in links:
        assert link.is_displayed()

    # 4. Проверяем, что текст первой ссылки содержит "1"
    assert "1" in links[0].text

    driver.quit()
