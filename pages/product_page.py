from .base_page import BasePage
from.locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def go_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.basket_btn)
        self.product_name=self.browser.find_element(*ProductPageLocators.product_name).text
        self.product_price=self.browser.find_element(*ProductPageLocators.product_price).text

        login_link.click()

    def basket_checked(self):
        product_name_in_basket = self.browser.find_elements(*ProductPageLocators.product_name_in_basket)
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.product_price_in_basket)
        assert self.product_name==product_name_in_basket[0].text, "names don't match"
        assert self.product_price==product_price_in_basket.text, "prices don't match"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented") 