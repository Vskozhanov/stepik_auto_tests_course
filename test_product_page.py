import pytest
from .product_page import ProductPage
import time
from .login_page import LoginPage
from .locators import BasketPageLocators
from .basket_page import BasketPage

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    page=ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):

    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):

    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    answer = page.solve_quiz_and_get_code()
    time.sleep(2)
    page.should_be_message_about_adding()
    page.basket_price()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    page=ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.should_disappear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page=LoginPage(browser,link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):

    link='http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page=BasketPage(browser,link)
    page.open()
    page.go_to_basket()
    page.should_be_current_url_basket()
    page.basket_is_empty()
    page.basket_message()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        email = str(time.time()) + "@fakemail.org"
        password = '657980SDF8d97fg980dsay6d87'
        link='http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page=LoginPage(browser,link)
        page.open()
        page.register_new_user(email,password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):

        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        time.sleep(3)
        page.should_be_message_about_adding()
        page.basket_price()






