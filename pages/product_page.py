from .base_page import BasePage
from .locators_product import BasketLocators

class Basket(BasePage):
    def add_book_to_basket(self):
        basket_btn = self.driver.find_element(*BasketLocators.BASKET_BTN)
        basket_btn.click()
        self.solve_quiz_and_get_code()

    def get_book_in_success_message(self):
        message_book = self.driver.find_element(*BasketLocators.MESSAGE_BOOK).text
        book_name = self.get_book_name()
        assert "Coders at Work has been added to your basket." in message_book, "Message doesn't contain book"

    def get_book_name(self):
        book_name = self.driver.find_element(*BasketLocators.BOOK_NAME).text
        print(book_name)
        return book_name

    def get_success_book_price(self):
        message_book = self.driver.find_element(*BasketLocators.MESSAGE_BOOK).text
        book_price = self.get_book_price()
        assert book_price in message_book, "Price isn't true"

    def get_book_price(self):
        book_price = self.driver.find_element(*BasketLocators.BOOK_PRICE).text
        print(book_price)
        return book_price
    
