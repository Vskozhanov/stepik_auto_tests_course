from .base_page import BasePage
from .locators import ProductPageLocators
from.locators import ProductLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button=self.browser.find_element(*ProductPageLocators.BASKET)
        button.click()

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE), 'Message is be away'
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), 'Book is be away'
        message=self.browser.find_element(*ProductPageLocators.MESSAGE).text
        book=self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert 'has been added to your basket.' in message, 'Message is not correct'


    def basket_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_BASKET), 'PRICE_B IS BE AWAY'
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), 'PRICE_PR IS BE AWAY'
        price_book=self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_basket=self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert price_book in price_basket, 'PRICE IS NOT CORRECT'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductLocators.SUCCESS_MESSAGE), 'Message is present'

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductLocators.SUCCESS_MESSAGE), 'Message is not disapeared'











