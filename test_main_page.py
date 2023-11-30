from selenium import webdriver
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(driver):
    driver = webdriver.Chrome()
    link = "http://selenium1py.pythonanywhere.com/"
    driver.get(link)
    login_link = driver.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
