from selenium import webdriver
from pages.shop_page import LoginPage, MainPage, CartPage, CheckoutPage
import allure


@allure.title("Тестирование работы интернет-магазина")
@allure.description("Тест проверяет корректность работы интернет-магазина")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    url = "https://www.saucedemo.com/"

    login_page = LoginPage(driver, url)
    with allure.step("Открытие страницы интернет-магазина"):
        login_page.open()
    with allure.step("Авторизация на странице магазина"):
        login_page.login("standard_user", "secret_sauce")

    main_page = MainPage(driver)
    with allure.step("Добавить товар в корзину"):
        main_page.add_to_cart("sauce-labs-backpack")
    with allure.step("Добавить товар в корзину"):
        main_page.add_to_cart("sauce-labs-bolt-t-shirt")
    with allure.step("Добавить товар в корзину"):
        main_page.add_to_cart("sauce-labs-onesie")
    with allure.step("Перейти в корзину"):
        main_page.go_to_cart()

    cart_page = CartPage(driver)
    with allure.step("Нажать на кнопку 'Checkout'"):
        cart_page.button_checkout()

    checkout_page = CheckoutPage(driver)
    with allure.step("Заполнить свои данные"):
        checkout_page.fill_form("Sergei", "S", "630073")
    with allure.step("Проверить итоговую сумму заказа"):
        checkout_page.verify_total("60.45")

    driver.quit()
