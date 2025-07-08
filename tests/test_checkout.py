# tests/test_checkout.py

import pytest
from screens.cart_screen import CartScreen
from screens.checkout_screen import CheckoutScreen
from screens.payment_screen import PaymentScreen
from screens.review_order_screen import ReviewOrderScreen
from screens.checkout_complete_screen import CheckoutCompleteScreen
from screens.login_screen import LoginScreen
from screens.products_screen import ProductsScreen
from screens.product_details_screen import ProductDetailsScreen
# The setup_cart_with_item fixture is now automatically available from conftest.py

@pytest.mark.checkout
def test_full_checkout_flow(setup_cart_with_item):
    """
    This test verifies the complete end-to-end checkout flow.
    """
    print("--- Starting test: test_full_checkout_flow ---")
    cart_screen, _ = setup_cart_with_item

    # --- Step 1: Proceed from Cart to Shipping ---
    cart_screen.proceed_to_checkout()

    # --- Step 1.5: Handle the login screen that appears during checkout ---
    print("Handling login required for checkout...")
    login_screen = LoginScreen(driver=cart_screen.driver)
    login_screen.enter_username("bob@example.com")
    login_screen.enter_password("10203040")
    login_screen.tap_login_button()

    # --- Step 2: Fill Shipping Address and proceed to Payment ---
    shipping_screen = CheckoutScreen(driver=cart_screen.driver)
    assert shipping_screen.is_checkout_title_displayed(), "Did not land on shipping address screen after checkout login."
    shipping_screen.fill_shipping_address(
        name="Rebecca Winter",
        address="Mandorley 112",
        city="Truro",
        zip_code="89750",
        country="United Kingdom"
    )
    shipping_screen.tap_to_payment_button()

    # --- Step 3: Fill Payment Details and proceed to Review ---
    payment_screen = PaymentScreen(driver=cart_screen.driver)
    payment_screen.fill_payment_details(
        name="Rebecca Winter",
        card_number="325812657568789",
        expiration="03/25",
        security_code="123"
    )
    payment_screen.tap_review_order_button()

    # --- Step 4: Place the order ---
    review_screen = ReviewOrderScreen(driver=cart_screen.driver)
    review_screen.tap_place_order_button()

    # --- Step 5: Verify the order is complete ---
    complete_screen = CheckoutCompleteScreen(driver=cart_screen.driver)
    assert complete_screen.is_checkout_complete_title_displayed(), "Checkout was not completed successfully."
    
    print("--- Finished test: test_full_checkout_flow ---")


@pytest.mark.checkout
@pytest.mark.negative
def test_checkout_with_empty_shipping_form(setup_cart_with_item):
    """
    This negative test verifies that appropriate error messages are shown
    when submitting an empty shipping address form.
    """
    print("--- Starting test: test_checkout_with_empty_shipping_form ---")
    cart_screen, _ = setup_cart_with_item

    # --- Step 1: Proceed from Cart to Shipping ---
    cart_screen.proceed_to_checkout()

    # --- Step 1.5: Handle the login screen that appears during checkout ---
    print("Handling login required for checkout...")
    login_screen = LoginScreen(driver=cart_screen.driver)
    login_screen.enter_username("bob@example.com")
    login_screen.enter_password("10203040")
    login_screen.tap_login_button()

    # --- Step 2: Tap 'To Payment' without filling the form ---
    shipping_screen = CheckoutScreen(driver=cart_screen.driver)
    shipping_screen.tap_to_payment_button()

    # --- Step 3: Verify that the error messages are displayed ---
    full_name_error = shipping_screen.get_full_name_error()
    address_error = shipping_screen.get_address_error()

    assert full_name_error == "Please provide your full name.", f"Incorrect full name error: {full_name_error}"
    assert address_error == "Please provide your address.", f"Incorrect address error: {address_error}"

    print("--- Finished test: test_checkout_with_empty_shipping_form ---")


@pytest.mark.checkout
@pytest.mark.negative
def test_checkout_with_empty_cart(driver):
    """
    This edge case verifies that the 'Proceed to Checkout' button
    is not present when the cart is empty.
    """
    print("--- Starting test: test_checkout_with_empty_cart ---")
    
    # --- Step 1: Ensure user is logged in and on the Products screen ---
    products_screen = ProductsScreen(driver)
    checkout_screen = CheckoutScreen(driver)
    login_screen = LoginScreen(driver)

    if not products_screen.is_products_title_displayed() and not checkout_screen.is_checkout_title_displayed():
        print("User is not logged in. Performing login.")
        login_screen.enter_username("bob@example.com")
        login_screen.enter_password("10203040")
        login_screen.tap_login_button()

    if checkout_screen.is_checkout_title_displayed():
        print("User on checkout screen, navigating to catalog.")
        checkout_screen.navigate_to_catalog()

    # --- Step 2: Add an item to the cart to set up the state ---
    print("Adding an item to the cart to set up the test state.")
    products_screen.select_backpack()
    product_details_screen = ProductDetailsScreen(driver)
    product_details_screen.add_to_cart()
    products_screen.tap_cart_icon()

    # --- Step 3: Verify the item is in the cart and then remove it ---
    cart_screen = CartScreen(driver)
    cart_screen.wait_for_screen_to_load()
    assert cart_screen.is_backpack_in_cart(), "Setup for empty cart test failed: Backpack not in cart."
    print("Item found in cart. Removing it.")
    cart_screen.remove_item()

    # --- Step 4: Verify the cart is now empty and checkout is not possible ---
    assert cart_screen.is_cart_empty(), "Cart is not empty after removal."
    assert not cart_screen.is_checkout_button_displayed(), "Checkout button was displayed for an empty cart."

    print("--- Finished test: test_checkout_with_empty_cart ---")
