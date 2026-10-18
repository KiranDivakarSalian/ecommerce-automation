from pages.base_page import BasePage


class InventoryPage(BasePage):
    CART_LINK = ".shopping_cart_link"
    CART_BADGE = ".shopping_cart_badge"

    def add_product_to_cart(self, product_name: str):
        product_card = self.page.locator(".inventory_item").filter(has_text=product_name)
        product_card.get_by_role("button", name="Add to cart").click()

    def open_cart(self):
        self.page.click(self.CART_LINK)

    def get_cart_count(self) -> int:
        badge = self.page.locator(self.CART_BADGE)
        if badge.count() == 0:
            return 0
        text = badge.text_content()
        return int(text.strip()) if text else 0
