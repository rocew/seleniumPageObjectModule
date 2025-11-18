from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.add_to_basket_btn = (By.CSS_SELECTOR, ".btn-add-to-basket")
        self.product_name = (By.CSS_SELECTOR, ".product_main h1")
        self.product_price = (By.CSS_SELECTOR, ".product_main .price_color")
        self.success_message = (
            By.CSS_SELECTOR, ".alert-success .alertinner strong")
        self.basket_total_message = (
            By.CSS_SELECTOR, ".alert-info .alertinner strong")
        self.success_messages = (By.CSS_SELECTOR, ".alert-success")
        self.success_message_selector = (By.CSS_SELECTOR, ".alert-success")

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*self.add_to_basket_btn)
        add_button.click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(*self.product_name).text

    def get_product_price(self):
        return self.browser.find_element(*self.product_price).text

    def get_success_message_product_name(self):
        return self.browser.find_element(*self.success_message).text

    def get_basket_total_message(self):
        return self.browser.find_element(*self.basket_total_message).text

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *self.add_to_basket_btn), "Add to basket button is not present"

    def should_be_success_message(self):
        assert self.is_element_present(
            *self.success_messages), "Success message is not present"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*self.success_message_selector), \
            "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*self.success_message_selector), \
            "Success message did not disappear, but should have"

    def should_be_correct_product_in_basket(self):
        product_name = self.get_product_name()
        basket_product_name = self.get_success_message_product_name()
        assert product_name == basket_product_name, \
            f"Product name in basket doesn't match. Expected: {product_name}, got: {basket_product_name}"

    def should_be_correct_basket_total(self):
        product_price = self.get_product_price()
        basket_total = self.get_basket_total_message()
        assert product_price == basket_total, \
            f"Basket total doesn't match product price. Expected: {product_price}, got: {basket_total}"
