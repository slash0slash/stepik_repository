from selenium.webdriver.common.by import By

class ProductPageLocators():
    BASKET_BTN = (By.CSS_SELECTOR, "form#add_to_basket_form.add-to-basket")
    MESSAGE_BOOK = (By.CSS_SELECTOR, "div#messages")
    BOOK_NAME = (By.CSS_SELECTOR, "div.alertinner")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input#id_registration-email.form-control")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input#id_registration-password1.form-control")
    PASSWORD_FIELD_AGAIN = (By.CSS_SELECTOR, "input#id_registration-password2.form-control")
    REGISTER_BTN = (By.NAME, "registration_submit")
