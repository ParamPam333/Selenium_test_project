from .base_page import BasePage
from.locators import BasketPageLocators as BP

class BasketPage(BasePage):
    def basket_is_empty(self):
        assert "Your basket is empty." in self.browser.find_element(*BP.BASKET_EMPTY_TEXT).text, 'Basket not empty'
            
