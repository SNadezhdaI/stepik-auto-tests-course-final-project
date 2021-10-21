from pages.main_page import MainPage
from pages.login_page import LoginPage

def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
    
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    
def test_login_and_registration_form_is_presented(browser):
    link_login = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page_login = LoginPage(browser, link_login)
    page_login.open()
    page_login.should_be_login_page()
    
    
    