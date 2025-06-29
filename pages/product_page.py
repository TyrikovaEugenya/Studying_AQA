from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_basket_button(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_FORM)

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_FORM)
        add_to_basket_button.click()
        
    def names_of_books_should_coincide(self):
        name_of_book = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        name_of_added_book = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_NAME).text
        assert name_of_book in name_of_added_book, "Names of books dont coincide"
        
    def prices_of_books_should_coincide(self):
        price_of_book = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        price_of_added_book = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_PRICE).text
        assert price_of_book in price_of_added_book, "Prices arent equal"