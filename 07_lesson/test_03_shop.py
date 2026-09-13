from selenium import webdriver
from shop_pages import LoginPage, MainPage, CartPage, CheckoutPage


def test_saucedemo_shop():
    driver = webdriver.Firefox()

    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    main_page.add_to_cart("Sauce Labs Backpack")
    main_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    main_page.add_to_cart("Sauce Labs Onesie")
    main_page.go_to_cart()

    cart_page.checkout()

    checkout_page.fill_form("Иван", "Иванов", "123456")
    total = checkout_page.get_total()

    driver.quit()

    assert total == "$58.29"
