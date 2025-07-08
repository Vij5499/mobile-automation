# tests/conftest.py

import pytest
from utils.driver_factory import get_android_driver

@pytest.fixture(scope="function")
def driver(request):
    """
    This fixture creates and returns an Appium driver instance for each test function.
    It also handles quitting the driver after the test has finished.
    """
    app_driver = get_android_driver()
    yield app_driver
    print("\n--- Tearing down Appium session ---")
    app_driver.quit()

@pytest.fixture(scope="function")
def setup_cart_with_item(driver):
    """
    This fixture ensures the user is logged in and has one
    Sauce Labs Backpack in the cart before each test that uses it.
    It yields the necessary screen objects for the tests to use.
    """
    # --- FIX: Move imports inside the fixture to prevent circular dependencies ---
    from screens.products_screen import ProductsScreen
    from screens.checkout_screen import CheckoutScreen
    from screens.cart_screen import CartScreen
    from screens.login_screen import LoginScreen
    from screens.product_details_screen import ProductDetailsScreen
    
    print("--- Fixture: Setting up cart with one item ---")
    products_screen = ProductsScreen(driver)
    checkout_screen = CheckoutScreen(driver)
    cart_screen = CartScreen(driver)

    # Ensure we are on the products screen
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
    
    # Add item to cart and navigate to the cart screen
    products_screen.select_backpack()
    product_details_screen = ProductDetailsScreen(driver)
    product_details_screen.add_to_cart()
    products_screen.tap_cart_icon()

    # Wait for the cart screen to load before verifying
    cart_screen.wait_for_screen_to_load()
    assert cart_screen.is_backpack_in_cart(), "Setup failed: Backpack not in cart."
    
    # Yield control to the test function
    yield cart_screen, products_screen

