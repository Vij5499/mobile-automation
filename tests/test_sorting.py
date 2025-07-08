# tests/test_sorting.py

import pytest
from screens.login_screen import LoginScreen
from screens.products_screen import ProductsScreen
from screens.checkout_screen import CheckoutScreen

@pytest.mark.sorting
def test_sort_products_by_price_ascending(driver):
    """
    This test case verifies that a user can successfully sort products
    by price from low to high.
    """
    print("--- Starting test: test_sort_products_by_price_ascending ---")

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

    # --- Step 2: Sort the products and get the price of the first item ---
    products_screen.sort_by_price_ascending()
    first_price = products_screen.get_first_item_price()

    # --- Step 3: Verify the price is correct ---
    expected_price = "$7.99"
    assert first_price == expected_price, f"Ascending sorting failed. Expected first price to be {expected_price}, but got {first_price}."

    print("--- Finished test: test_sort_products_by_price_ascending ---")


@pytest.mark.sorting
def test_sort_products_by_price_descending(driver):
    """
    This test case verifies that a user can successfully sort products
    by price from high to low.
    """
    print("--- Starting test: test_sort_products_by_price_descending ---")

    # --- Step 1: Ensure user is logged in and on the Products screen ---
    products_screen = ProductsScreen(driver)
    checkout_screen = CheckoutScreen(driver)

    if not products_screen.is_products_title_displayed():
        # If not on products screen, navigate or log in
        if checkout_screen.is_checkout_title_displayed():
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

    # --- Step 2: Sort the products and get the price of the first item ---
    products_screen.sort_by_price_descending()
    first_price = products_screen.get_first_item_price()

    # --- Step 3: Verify the price is correct ---
    expected_price = "$49.99" # Price of the most expensive item
    assert first_price == expected_price, f"Descending sorting failed. Expected first price to be {expected_price}, but got {first_price}."

    print("--- Finished test: test_sort_products_by_price_descending ---")

