from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, item_name):
        formatted_name = item_name.lower().replace(" ", "-")
        button_locator = (
            By.ID, f"add-to-cart-{formatted_name}"
        )
        self.driver.find_element(*button_locator).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total(self):
        total_text = self.driver.find_element(*self.total_label).text
        return total_text.split("Total: ")[1]
