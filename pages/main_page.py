from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators_product import BasketLocators
class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.driver.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_in_basket(self):
        assert self.is_element_present(*BasketLocators.BOOK_IN_BASKET), "Book isn't in basket"

    def should_be_price(self):
        assert self.is_element_present(*BasketLocators.BASKET_PRICE), "Price isn't true"
