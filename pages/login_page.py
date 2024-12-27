from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, '"Login" not in URL'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_field), "Login field is not presented"
        assert self.is_element_present(*LoginPageLocators.PASS_field), "Pass field is not presented"
        assert self.is_element_present(*LoginPageLocators.lOGIN_BTN), "Login button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_field_reg), "Regestration email field is not presented"
        assert self.is_element_present(*LoginPageLocators.PASS_field_reg), "Regestration pass field is not presented"
        assert self.is_element_present(*LoginPageLocators.PASS_field_reg2), "Regestration repit pass field is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_BTN), "Regestration button is not presented"

    def register_new_user(self, email, password):
        reg_email=self.browser.find_element(*LoginPageLocators.EMAIL_field_reg)
        reg_email.send_keys(email)
        reg_pass=self.browser.find_element(*LoginPageLocators.PASS_field_reg)
        reg_pass2=self.browser.find_element(*LoginPageLocators.PASS_field_reg2)
        reg_pass.send_keys(password)
        reg_pass2.send_keys(password)
        reg_btn=self.browser.find_element(*LoginPageLocators.REG_BTN)
        reg_btn.click()