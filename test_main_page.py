from selenium.webdriver.common.by import By
import time

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    time.sleep(5)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()