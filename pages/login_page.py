from config.settings import BASE_URL
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = ".error-message-container"

    def open(self, url=BASE_URL):
        self.page.goto(url)
        self.page.wait_for_load_state("domcontentloaded")

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.page.locator(self.ERROR_MESSAGE).text_content()
