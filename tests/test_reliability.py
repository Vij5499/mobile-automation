# tests/test_reliability.py

import pytest
import time
from screens.cart_screen import CartScreen
from screens.checkout_screen import CheckoutScreen
from screens.login_screen import LoginScreen

@pytest.mark.reliability
def test_app_state_after_backgrounding(setup_cart_with_item):
    """
    This reliability test verifies that the app maintains its state and
    user-entered data after being sent to the background and reopened.
    """
    print("--- Starting test: test_app_state_after_backgrounding ---")
    cart_screen, _ = setup_cart_with_item
    driver = cart_screen.driver # Get the driver from the fixture

    # --- Step 1: Navigate to the shipping address screen ---
    cart_screen.proceed_to_checkout()
    login_screen = LoginScreen(driver)
    login_screen.enter_username("bob@example.com")
    login_screen.enter_password("10203040")
    login_screen.tap_login_button()

    # --- Step 2: Enter data into a form field ---
    shipping_screen = CheckoutScreen(driver)
    assert shipping_screen.is_checkout_title_displayed(), "Did not land on shipping address screen."
    
    test_name = "Test Name"
    shipping_screen.send_keys_to_element(shipping_screen._full_name_input, test_name)
    print(f"Entered '{test_name}' into the full name field.")

    # --- Step 3: Send the app to the background and wait ---
    print("Sending app to background for 5 seconds...")
    driver.background_app(seconds=5)
    print("Bringing app back to foreground.")
    # Note: activate_app is implicitly called when the background time is up.

    # --- Step 4: Verify the data is still present ---
    entered_text = shipping_screen.get_full_name_text()
    print(f"Text found in field after backgrounding: '{entered_text}'")
    
    assert entered_text == test_name, "App did not retain form data after being backgrounded."

    print("--- Finished test: test_app_state_after_backgrounding ---")

