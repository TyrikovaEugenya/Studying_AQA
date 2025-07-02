from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, "div.basket-mini a.btn")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    RGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_TO_BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    BOOK_NAME = (By.CSS_SELECTOR, "ul.breadcrumb li.active")
    ADDED_BOOK_NAME = (By.CSS_SELECTOR, "div#messages strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    ADDED_BOOK_PRICE = (By.CSS_SELECTOR, "div#messages p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert-success:nth-child(1)")
    
class BasketPageLocators():
    BASKET_FORM = (By.CSS_SELECTOR, "div.content form.basket_summary")
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div#content_inner p")
    BASKET_IS_EMPTY_NOW_MESSAGE = (By.CSS_SELECTOR, "div#messages div.alert-info")