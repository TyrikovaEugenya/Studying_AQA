from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver
import random
import string


def generate_random_email(domain="example.com", lenght=10):
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=lenght))
    return f"{random_string}@{domain}"

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Url is incorrect"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form isnt present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.RGISTER_FORM), "Register form isnt present"
        
    def register_new_user(self, password="TestPassord123!"):
        email = generate_random_email()
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        password1_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        password2_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        
        email_input.send_keys(email)
        password1_input.send_keys(password)
        password2_input.send_keys(password)
        register_button.click()