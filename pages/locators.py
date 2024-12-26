from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_field = (By.CSS_SELECTOR, "input[name=login-username]")
    PASS_field = (By.CSS_SELECTOR, "input[name=login-password]")
    lOGIN_BTN = (By.CSS_SELECTOR, "button[name=login_submit]")

    EMAIL_field_reg = (By.CSS_SELECTOR, "input[name=registration-email]")
    PASS_field_reg = (By.CSS_SELECTOR, "input[name=registration-password1]")
    PASS_field_reg2 = (By.CSS_SELECTOR, "input[name=registration-password2]")
    REG_BTN=(By.CSS_SELECTOR, "button[name=registration_submit]")

