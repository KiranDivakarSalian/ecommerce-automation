import os

STANDARD_USERNAME = os.getenv("SAUCE_USERNAME", "standard_user")
STANDARD_PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")

CHECKOUT_CUSTOMER = {
    "first_name": "Kiran",
    "last_name": "Tester",
    "postal_code": "576101",
}
