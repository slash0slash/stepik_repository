from selenium.webdriver.common.by import By

class BasketLocators():
    BASKET_BTN = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    MESSAGE_BOOK = (By.CSS_SELECTOR, "div#messages")
    BOOK_NAME = (By.CSS_SELECTOR, "div.alertinner")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")

