# tests/test_price_calculation.py

import pytest
# FIX: All imports are absolute from the project root.
from screens.login_screen import LoginScreen
from screens.products_screen import ProductsScreen
from screens.checkout_screen import CheckoutScreen
from screens.cart_screen import CartScreen
from screens.product_details_screen import ProductDetailsScreen

def get_price_as_float(price_str):
    """Helper function to convert a price string like '$29.99' to a float."""
    return float(price_str.replace('$', ''))

@pytest.mark.data_validation
def test_total_price_calculation(driver):
    """
    This test verifies that the total price in the cart is calculated correctly.
    """
    print("--- Starting test: test_total_price_calculation ---")

    # --- Step 1: Ensure user is logged in and on the Products screen ---
    products_screen = ProductsScreen(driver)
    checkout_screen = CheckoutScreen(driver)

    if not products_screen.is_products_title_displayed():
        if checkout_screen.is_checkout_title_displayed():
            checkout_screen.navigate_to_catalog()
        else:
            login_screen = LoginScreen(driver)
            login_screen.enter_username("bob@example.com")
            login_screen.enter_password("10203040")
            login_screen.tap_login_button()
            assert checkout_screen.is_checkout_title_displayed()
            checkout_screen.navigate_to_catalog()

    # --- Step 2: Add two different items to the cart ---
    # Add backpack
    products_screen.select_backpack()
    product_details_screen = ProductDetailsScreen(driver)
    product_details_screen.add_to_cart()
    # Go back to the products list
    driver.back() 
    
    # Add bike light
    products_screen.select_bike_light()
    product_details_screen.add_to_cart()

    # --- Step 3: Navigate to cart and get prices ---
    products_screen.tap_cart_icon()
    cart_screen = CartScreen(driver)
    cart_screen.wait_for_screen_to_load()

    backpack_price_str = cart_screen.get_backpack_price()
    bike_light_price_str = cart_screen.get_bike_light_price()
    total_price_str = cart_screen.get_total_price()

    # --- Step 4: Convert prices to numbers and verify the calculation ---
    backpack_price = get_price_as_float(backpack_price_str)
    bike_light_price = get_price_as_float(bike_light_price_str)
    total_price = get_price_as_float(total_price_str)

    expected_total = backpack_price + bike_light_price
    assert total_price == expected_total, f"Total price calculation is incorrect. Expected {expected_total}, but got {total_price}."

    print("--- Finished test: test_total_price_calculation ---")

