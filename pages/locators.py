from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "a#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form.well")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form.well")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "div#content_inner")
    USER_ICON = (By.CSS_SELECTOR, "div.alert.alert-success.fade.in")
