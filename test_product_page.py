from .pages.product_page import ProductPage
import pytest
from.pages.locators import ProductPageLocators, BasketPageLocators
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


import time

@pytest.mark.reg_guest
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link="http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)   
        page.open() 
        page.register_new_user(str(time.time()) + "@fakemail.org", 'abcd123456789')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser): 
        link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)   
        page.open() 
        assert page.is_not_element_present(*ProductPageLocators.succ_message), \
        "Success message is presented, but should not be"    

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
        page = ProductPage(browser, link)   
        page.open()   
        page.go_to_basket()
        page.solve_quiz_and_get_code()
        page.basket_checked()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = link
    page = ProductPage(browser, link)   
    page.open()   
    page.go_to_basket()
    page.solve_quiz_and_get_code()
    page.basket_checked()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   
    page.open()   
    page.go_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.succ_message), \
       "Success message is presented, but should not be"

def test_guest_cant_see_success_message(browser): 
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   
    page.open() 
    assert page.is_not_element_present(*ProductPageLocators.succ_message), \
       "Success message is presented, but should not be"

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   
    page.open()  
    page.go_to_basket()
    assert page.is_disappeared(*ProductPageLocators.succ_message), \
    "Success message is presented, but should not be"

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page=BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    assert page.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
       "Product in basket"
    page.basket_is_empty()
    