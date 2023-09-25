from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM=(By.CSS_SELECTOR, '#register_form')
    EMAIL=(By.CSS_SELECTOR,'#id_registration-email')
    PASSWORD1=(By.CSS_SELECTOR,'#id_registration-password1')
    PASSWORD2=(By.CSS_SELECTOR,'#id_registration-password2')
    BUTTON_FOR_REGISTER=(By.CSS_SELECTOR,"[name='registration_submit']")

class ProductPageLocators():
    BASKET=(By.CSS_SELECTOR, '.btn-add-to-basket')
    BOOK_NAME=(By.CSS_SELECTOR, 'div.product_main h1')
    PRICE_BASKET=(By.CSS_SELECTOR,'.alert-info .alertinner strong')
    PRICE_PRODUCT=(By.CSS_SELECTOR,'.product_main .price_color')
    MESSAGE=(By.CSS_SELECTOR,'div.alertinner')


class ProductLocators():
    SUCCESS_MESSAGE=(By.CSS_SELECTOR,'div.alertinner')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_BUTTON=(By.CSS_SELECTOR, '.btn-group .btn.btn-default')
    MESSAGE_FROM_BASKET=(By.CSS_SELECTOR,'#content_inner p')
    BASKET_FULL=(By.CSS_SELECTOR,'#basket_formset')





