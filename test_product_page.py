from .pages.product_page import ProductPage
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_basket_button()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.names_of_books_should_coincide()
    product_page.prices_of_books_should_coincide()