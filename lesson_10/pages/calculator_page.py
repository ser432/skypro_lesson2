from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:

    def __init__(self, driver: WebDriver, url: str) -> None:
        """
        Конструктор класса CalculatorPage.
        :param driver: WebDriver — объект драйвера Selenium.
        :param url: str — адрес страницы.
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 45)

    @allure.step("Открытие страницы калькулятора")
    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(self.url)

    @allure.step("Установка задержки {delay_time} секунд")
    def set_delay(self, delay_time: str) -> None:
        """
        Устанавливает задержку для выполнения операций на калькуляторе.
        :param delay_time: str — время задержки в секундах.
        """
        delay_field = self.driver.find_element(By.ID, "delay")
        delay_field.clear()
        delay_field.send_keys(delay_time)

    @allure.step("Нажатие кнопки '{button_value}'")
    def click_button(self, button_value: str) -> None:
        """
        Нажимает на кнопку калькулятора.
        :param button_value: str — текст на кнопке.
        """
        xpath = f"//span[text()='{button_value}']"
        self.driver.find_element(By.XPATH, xpath).click()

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self) -> str:
        """
        Возвращает текущий результат с экрана калькулятора.
        :return: str — текст результата.
        """
        self.wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
