# tests/test_login.py

import pytest
from screens.login_screen import LoginScreen
from screens.products_screen import ProductsScreen
from screens.checkout_screen import CheckoutScreen

@pytest.mark.login
def test_successful_login(driver):
    """
    This test case verifies that a user can successfully log in
    with valid credentials. This is our 'happy path' test.
    """
    print("--- Starting test: test_successful_login ---")

    products_screen = ProductsScreen(driver)
    if products_screen.is_products_title_displayed():
        print("User is already logged in. Performing logout first.")
        products_screen.perform_logout()

    login_screen = LoginScreen(driver)
    login_screen.enter_username("bob@example.com")
    login_screen.enter_password("10203040")
    login_screen.tap_login_button()
    
    checkout_screen = CheckoutScreen(driver)
    assert checkout_screen.is_checkout_title_displayed(), "Login failed: Checkout screen was not displayed."
    print("--- Finished test: test_successful_login ---")


@pytest.mark.login
def test_failed_login_with_wrong_password(driver):
    """
    This test case verifies that an error message is shown for invalid
    credentials. This is our 'negative path' test.
    """
    print("--- Starting test: test_failed_login_with_wrong_password ---")

    products_screen = ProductsScreen(driver)
    if products_screen.is_products_title_displayed():
        print("User is already logged in. Performing logout first.")
        products_screen.perform_logout()

    login_screen = LoginScreen(driver)
    login_screen.enter_username("bob@example.com")
    login_screen.enter_password("wrong_password")
    login_screen.tap_login_button()

    assert login_screen.is_error_message_displayed(), "Error message was not displayed for failed login."
    print("--- Finished test: test_failed_login_with_wrong_password ---")

@pytest.mark.login
@pytest.mark.negative
def test_login_with_non_existent_user(driver):
    """
    This negative test verifies that an error message is shown when
    attempting to log in with a user that does not exist.
    """
    print("--- Starting test: test_login_with_non_existent_user ---")

    products_screen = ProductsScreen(driver)
    if products_screen.is_products_title_displayed():
        print("User is already logged in. Performing logout first.")
        products_screen.perform_logout()

    login_screen = LoginScreen(driver)
    login_screen.enter_username("nobody@example.com")
    login_screen.enter_password("anypassword")
    login_screen.tap_login_button()

    assert login_screen.is_error_message_displayed(), "Error message was not displayed for non-existent user."
    print("--- Finished test: test_login_with_non_existent_user ---")

