from .pages.product_page import Basket
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
   

    
