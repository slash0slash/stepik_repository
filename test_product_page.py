from .pages.product_page import Basket
from .pages.basket_page import BasketPage
from .pages.base_page import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6",
                                 pytest.param("7", marks=pytest.mark.xfail),
                                 "8", "9"])
def test_guest_can_add_product_to_basket(driver, link):
    link = (f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}")
    page = Basket(driver, link)
    page.open()
    page.add_book_to_basket()
    page.get_book_in_success_message()
    page.get_book_name()
    page.get_success_book_price()
    page.get_book_price()

def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = Basket(driver, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(driver, link)
    page.open()
    page.go_to_basket()
    page.should_not_be_from_product_page()
   
