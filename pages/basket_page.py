from .base_page import BasePage
from .locators_product import ProductPageLocators
from .locators import BasePageLocators

class BasketPage(BasePage):
    def should_not_be_from_main_page(self):
        basket_is_empty = self.driver.find_element(*BasePageLocators.BASKET_IS_EMPTY).text
        assert "Your basket is empty." in basket_is_empty, "Basket isn't empty"

    def should_not_be_from_product_page(self):
        basket_is_empty = self.driver.find_element(*BasePageLocators.BASKET_IS_EMPTY).text
        assert "Your basket is empty." in basket_is_empty, "Basket isn't empty"
        
