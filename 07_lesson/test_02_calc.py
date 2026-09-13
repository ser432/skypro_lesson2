from selenium import webdriver
from calculator_page import CalculatorPage


def test_slow_calculator():
    driver = webdriver.Chrome()
    calc_page = CalculatorPage(driver)

    calc_page.open()
    calc_page.set_delay(45)

    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    result = calc_page.get_result(timeout=50)

    driver.quit()
    assert result == "15"
