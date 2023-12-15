from .base_page import BasePage
from .locators import LoginPageLocators
from .locators_product import ProductPageLocators
from .locators import BasePageLocators 


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.driver.current_url, "URL ist'n correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        
    def register_new_user(self, email, password, password_again):
        email_field = self.driver.find_element(*ProductPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.driver.find_element(*ProductPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        password_field_again = self.driver.find_element(*ProductPageLocators.PASSWORD_FIELD_AGAIN)
        password_field_again.send_keys(password_again)
        register_btn = self.driver.find_element(*ProductPageLocators.REGISTER_BTN)
        register_btn.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented"
    
