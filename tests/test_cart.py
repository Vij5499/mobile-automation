# tests/test_cart.py

import pytest
from screens.login_screen import LoginScreen
from screens.products_screen import ProductsScreen
from screens.checkout_screen import CheckoutScreen
from screens.cart_screen import CartScreen
from screens.product_details_screen import ProductDetailsScreen

@pytest.mark.cart
def test_add_item_to_cart(driver):
    """
    This test case verifies that a user can add an item to the cart
    by navigating through the correct product details flow.
    """
    print("--- Starting test: test_add_item_to_cart ---")

    # --- Step 1: Ensure user is logged in and on the Products screen ---
    products_screen = ProductsScreen(driver)
    checkout_screen = CheckoutScreen(driver)

    if products_screen.is_products_title_displayed():
        print("User is already on the Products screen. Proceeding.")
    elif checkout_screen.is_checkout_title_displayed():
        print("User is on the Checkout screen. Navigating to catalog.")
        checkout_screen.navigate_to_catalog()
    else:
        print("User is not logged in. Performing full login and navigation.")
        login_screen = LoginScreen(driver)
        login_screen.enter_username("bob@example.com")
        login_screen.enter_password("10203040")
        login_screen.tap_login_button()
        assert checkout_screen.is_checkout_title_displayed(), "Did not land on checkout screen after login."
        checkout_screen.navigate_to_catalog()

    # --- Step 2: Select product, add to cart, and navigate to cart ---
    products_screen.select_backpack()
    
    product_details_screen = ProductDetailsScreen(driver)
    product_details_screen.add_to_cart()
    
    products_screen.tap_cart_icon()

    # --- Step 3: Verify the item is in the cart ---
    cart_screen = CartScreen(driver)
    assert cart_screen.is_backpack_in_cart(), "Backpack was not found in the cart after being added."

    print("--- Finished test: test_add_item_to_cart ---")

