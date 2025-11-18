from .base_page import BasePage
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def should_be_basket_url(self):
        # Проверка, что мы на странице корзины
        assert "basket" in self.browser.current_url, "Not on basket page"

    def should_be_empty_basket(self):
        # Проверка, что корзина пуста
        self.should_be_empty_message()
        self.should_not_be_items_in_basket()

    def should_be_empty_message(self):
        # Проверка наличия сообщения о пустой корзине
        assert self.is_element_present(By.CSS_SELECTOR, "#content_inner p"), \
            "Empty basket message is not presented"

        # Проверка текста сообщения
        empty_message = self.browser.find_element(
            By.CSS_SELECTOR, "#content_inner p").text
        assert "Your basket is empty" in empty_message or "Ваша корзина пуста" in empty_message, \
            f"Wrong empty message: {empty_message}"

    def should_not_be_items_in_basket(self):
        # Отрицательная проверка: товаров в корзине нет
        assert self.is_not_element_present(By.CSS_SELECTOR, ".basket-items"), \
            "Items are in basket, but should not be"
