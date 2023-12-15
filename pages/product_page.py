from .base_page import BasePage
from .locators_product import ProductPageLocators
from .locators import BasePageLocators

class ProductPage(BasePage):
    def add_book_to_basket(self):
        basket_btn = self.driver.find_element(*ProductPageLocators.BASKET_BTN)
        basket_btn.click()
        self.solve_quiz_and_get_code()

    def get_book_in_success_message(self):
        message_book = self.driver.find_element(*ProductPageLocators.MESSAGE_BOOK).text
        book_name = self.get_book_name()
        assert "Coders at Work has been added to your basket." in message_book, "Message doesn't contain book"

    def get_book_name(self):
        book_name = self.driver.find_element(*ProductPageLocators.BOOK_NAME).text
        print(book_name)
        return book_name

    def get_success_book_price(self):
        message_book = self.driver.find_element(*ProductPageLocators.MESSAGE_BOOK).text
        book_price = self.get_book_price()
        assert book_price in message_book, "Price isn't true"

    def get_book_price(self):
        book_price = self.driver.find_element(*ProductPageLocators.BOOK_PRICE).text
        print(book_price)
        return book_price
    
    def should_not_be_success_message(self):
        message_book = self.get_book_in_success_message()
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_BOOK), "Success message is presented, but should not be"

    def dont_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def not_success_message(self):
        message_book = self.get_book_in_success_message()
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_BOOK), "Success message is presented, but should not be"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login and link aren't presented"
        
