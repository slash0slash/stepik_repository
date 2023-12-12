from .pages.product_page import Basket
from .pages.base_page import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
  
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = Basket(driver, link)
    page.open()
    page.add_book_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = Basket(driver, link)
    page.open()
    page.dont_see_success_message()

def test_message_disappeared_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = Basket(driver, link)
    page.open()
    page.add_book_to_basket()
    page.not_success_message()
