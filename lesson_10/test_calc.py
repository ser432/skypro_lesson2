from selenium import webdriver
from pages.calculator_page import CalculatorPage
import allure


@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет корректность работы калькулятора")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc():
    driver = webdriver.Chrome()
    driver.maximize_window()

    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    calc_page = CalculatorPage(driver, url)

    with allure.step("Открытие страницы калькулятора"):
        calc_page.open()
    with allure.step("Установка задержки в секундах"):
        calc_page.set_delay("45")
    with allure.step("Нажать на кнопку '7'"):
        calc_page.click_button("7")
    with allure.step("Нажать на кнопку '+'"):
        calc_page.click_button("+")
    with allure.step("Нажать на кнопку '8'"):
        calc_page.click_button("8")
    with allure.step("Нажать на кнопку '='"):
        calc_page.click_button("=")

    with allure.step("Получение результата"):
        result_text = calc_page.get_result()
    with allure.step("Проверка результата"):
        assert result_text == "15"

    driver.quit()
