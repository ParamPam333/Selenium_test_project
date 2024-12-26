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

class ProductPageLocators():
    basket_btn = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    product_name = (By.CSS_SELECTOR, "div.col-sm-6 h1")
    product_price=(By.CSS_SELECTOR, "div.col-sm-6 p.price_color")
    product_name_in_basket=(By.CSS_SELECTOR, "div.alert-safe div.alertinner strong")
    product_price_in_basket=(By.CSS_SELECTOR, "div.alert-info div.alertinner strong")
    succ_message=(By.CSS_SELECTOR, "div#messages .alert ")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")