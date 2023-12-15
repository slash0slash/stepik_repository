from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.base_page import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(driver, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "vbuoWI56487NF!"
        password_again = password
        page.register_new_user(email, password, password_again)
        page.should_be_authorized_user()
        self.product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        page = ProductPage(driver, self.product_link)
        page.open()
        page.add_book_to_basket()
        page.get_book_in_success_message()
        page.get_book_name()
        page.get_success_book_price()
        page.get_book_price()

    def test_user_cant_see_success_message(self, driver):
        page = ProductPage(driver, self.product_link)
        page.open()
        page.dont_see_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(driver, link)
    page.open()
    page.add_book_to_basket()
    page.get_book_in_success_message()
    page.get_book_name()
    page.get_success_book_price()
    page.get_book_price()

def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = LoginPage(driver, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(driver, link)
    page.open()
    page.go_to_basket()
    page.should_not_be_from_product_page()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(driver, link)
    page.open()
    page.add_book_to_basket()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(driver, link)
    page.open()
    page.add_book_to_basket()
    page.not_success_message()
   
