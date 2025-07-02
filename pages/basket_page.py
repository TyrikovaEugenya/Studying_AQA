from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def no_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM), "Basket isnt empty"
        
    def basket_is_empty_message_present(self):
        #assert "Ваша корзина пуста" in self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE).text, "Basket is empty message isnt present"
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE)