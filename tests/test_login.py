from pages.login_page import LoginPage
from test_data.test_users import STANDARD_PASSWORD, STANDARD_USERNAME


def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)

    assert "/inventory.html" in page.url
   
    

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("invalid_user", "wrong_password")

    error_message = login_page.get_error_message()
    assert "Username and password do not match" in error_message
