import faker

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def registry_new_user(self):
        f = faker.Faker()
        email = f.email()

        self.browser.find_element(*LoginPageLocators.REGISTRY_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRY_PASSWORD_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRY_PASSWORD_CONFIRM).send_keys(email)

        registry_btn = self.browser.find_element(*LoginPageLocators.REGISTRY_BUTTON)

        registry_btn.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_parameter = "login"
        assert login_parameter in self.browser.current_url, "Incorrect url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRY_FORM), "Registry form is not presented"
