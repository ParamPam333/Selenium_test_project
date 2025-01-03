from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from.pages.locators import BasketPageLocators
import pytest
import time

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   
        login_page=LoginPage(browser, browser.current_url)
        page.open()   
        page.go_to_login_page()
        login_page.should_be_login_page()


    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page=BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    assert page.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
       "Product in basket"
    page.basket_is_empty()
    

