from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    # Запускаем браузер Chrome
    driver = webdriver.Chrome()

    # 1. Открываем страницу с динамической загрузкой
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Находим кнопку "Start" по CSS-селектору и кликаем
    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()

    # 3. Настраиваем явное ожидание (максимум 10 секунд)
    wait = WebDriverWait(driver, 10)

    # Ждем, пока элемент с текстом "Hello World!" станет видимым на странице
    hello_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )

    # 4. Делаем скриншот страницы
    driver.save_screenshot("06_lesson/screenshot_task1.png")

    # 5. Проверяем с помощью assert,
    # что текст элемента действительно равен "Hello World!"
    assert hello_element.text == "Hello World!"

    # Закрываем браузер
    driver.quit()
