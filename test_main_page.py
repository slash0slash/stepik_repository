from .pages.main_page import MainPage
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, link)
    page.open()
    page.go_to_login_page()
