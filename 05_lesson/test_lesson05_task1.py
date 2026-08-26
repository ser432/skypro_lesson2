from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    base_url = "https://httpbin.qa-territory.online"

    # 1. Открываем главную страницу
    driver.get(base_url)

    # 2. Находим и кликаем по ссылке "HTML Form"
    form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
    form_link.click()

    # 3. Проверяем, что URL изменился на /forms/post
    assert "/forms/post" in driver.current_url

    # 4. Возвращаемся назад
    driver.back()

    # 5. Проверяем, что вернулись на исходный URL
    assert driver.current_url.rstrip("/") == base_url.rstrip("/")

    driver.quit()
