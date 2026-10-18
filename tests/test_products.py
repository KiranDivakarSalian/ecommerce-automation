from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from test_data.test_users import CHECKOUT_CUSTOMER


def test_add_product_and_checkout(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    assert inventory_page.get_cart_count() == 1

    inventory_page.open_cart()
    cart_page = CartPage(authenticated_page)
    cart_page.checkout()

    checkout_page = CheckoutPage(authenticated_page)
    checkout_page.enter_customer_information(
        CHECKOUT_CUSTOMER["first_name"],
        CHECKOUT_CUSTOMER["last_name"],
        CHECKOUT_CUSTOMER["postal_code"],
    )

    assert "/checkout-step-two.html" in authenticated_page.url
