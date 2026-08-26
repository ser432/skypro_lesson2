from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    # 1. Находим поле по имени и вводим имя
    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Alex")

    # 2. Находим кнопку Submit по тексту в XPath и нажимаем
    submit_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Submit')]"
    )
    submit_button.click()

    # 3. Проверяем, что URL изменился на /post
    assert "/post" in driver.current_url

    driver.quit()
