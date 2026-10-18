from pages.inventory_page import InventoryPage


def test_authenticated_cart(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.add_product_to_cart("Sauce Labs Bike Light")

    assert inventory_page.get_cart_count() == 1
    assert "/inventory.html" in authenticated_page.url
