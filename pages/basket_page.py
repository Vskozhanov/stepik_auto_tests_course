from .base_page import BasePage
from.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_current_url_basket(self):
        url=self.browser.current_url
        assert 'basket' in url, 'THIS IS NOT BASKET PAGE'

    def basket_message(self):
        message=self.browser.find_element(*BasketPageLocators.MESSAGE_FROM_BASKET).text
        assert 'basket is empty' in message,'BASKET IS NOT EMPTY'

    def basket_is_empty(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_FULL),'BASKET IS NOT EMPTY'


