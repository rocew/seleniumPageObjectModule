import pytest
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestProductPage:

    @pytest.mark.xfail(reason="Сообщение об успехе появляется после добавления товара - это ожидаемое поведение")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        """
        Проверяем, что нет сообщения об успехе после добавления товара в корзину
        Этот тест должен падать, потому что сообщение ДОЛЖНО появляться
        """
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        """
        Проверяем, что нет сообщения об успехе при открытии страницы товара
        Этот тест должен проходить
        """
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="Сообщение об успехе не исчезает - это баг")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        """
        Проверяем, что сообщение об успехе исчезает после добавления товара в корзину
        Этот тест должен падать, потому что сообщение не исчезает (баг)
        """
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_success_message_disappear()
