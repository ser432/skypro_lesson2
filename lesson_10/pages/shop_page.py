from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure


class LoginPage:
    def __init__(self, driver: WebDriver, url: str) -> None:
        """
        Конструктор класса LoginPage.
        :param driver: WebDriver — объект драйвера Selenium.
        :param url: str — адрес страницы.
        """
        self.driver = driver
        self.url = url

    @allure.step("Открытие страницы магазина")
    def open(self) -> None:
        """
        Открывает страницу магазина.
        """
        self.driver.get(self.url)

    @allure.step("Авторизация на странице магазина")
    def login(self, username: str, password: str) -> None:
        """
        Авторизация на странице магазина.
        :param username: str — логин пользователя.
        :param password: str — пароль пользователя.
        """
        self.driver.find_element(By.ID, 'user-name').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'login-button').click()


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса MainPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Добавление товара в корзину")
    def add_to_cart(self, product_name: str) -> None:
        """
        Добавление товара в корзину.
        :param product_name: str — наименование товара.
        """
        self.driver.find_element(
            By.XPATH, f"//button[text()='Add to cart' and '{product_name}']").click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """
        Переходит в корзину.
        """
        self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()


class CartPage:
    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса CartPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Нажатие на кнопку Checkout")
    def button_checkout(self) -> None:
        """
        Переходит к оформлению заказа.
        """
        self.driver.find_element(By.ID, "checkout").click()

    @allure.step("Проверка товаров в корзине")
    def verify_cart_contents(self, expected_items: list) -> None:
        """
        Проверка товаров в корзине.
        :param expected_items: list — список товаров, которые должны быть в корзине.
        """
        cart_items = self.driver.find_elements(By.CLASS_NAME, 'cart_item')
        actual_items = [item.text for item in cart_items]
        for item in expected_items:
            assert item in actual_items, f"Товар {item} отсутствует в корзине"


class CheckoutPage:
    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса CheckoutPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Заполнение своих данных")
    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполнение своих данных.
        :param first_name: str — имя.
        :param last_name: str — фамилия.
        :param postal_code: str — почтовый индекс.
        """
        self.driver.find_element(By.ID, 'first-name').send_keys(first_name)
        self.driver.find_element(By.ID, 'last-name').send_keys(last_name)
        self.driver.find_element(By.ID, 'postal-code').send_keys(postal_code)
        self.driver.find_element(By.ID, 'continue').click()

    @allure.step("Проверка итоговой суммы")
    def verify_total(self, expected_total: str) -> None:
        """
        Проверка итоговой суммы.
        :param expected_total: str — ожидаемая итоговая сумма.
        """
        total_element = self.driver.find_element(
            By.CLASS_NAME, 'summary_total_label')
        actual_total = total_element.text.split("$")[-1]
        assert actual_total == expected_total, (
            f"Итоговая стоимость {actual_total} не совпадает с ожидаемой {expected_total}"
        )
