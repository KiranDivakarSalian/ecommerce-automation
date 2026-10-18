from pages.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BUTTON = "[data-test='checkout']"

    def checkout(self):
        self.page.click(self.CHECKOUT_BUTTON)
