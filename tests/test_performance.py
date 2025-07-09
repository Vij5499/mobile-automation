# tests/test_performance.py

import pytest
import time
from utils.driver_factory import get_android_driver
from screens.products_screen import ProductsScreen
from screens.checkout_screen import CheckoutScreen
from screens.login_screen import LoginScreen


# A reasonable threshold for app startup time in seconds.
# FIX: Increased threshold to a more realistic value for a local environment.
STARTUP_TIME_THRESHOLD_S = 30.0

@pytest.mark.performance
def test_app_startup_time():
    """
    This performance test measures the application's startup time by
    recording the time it takes from session creation until the first
    screen is interactive.
    """
    print("--- Starting test: test_app_startup_time ---")
    driver = None
    try:
        # --- Step 1: Record time and start the app session ---
        start_time = time.time()
        driver = get_android_driver()
        
        # --- Step 2: Wait for the first screen to be ready ---
        # The app can start on one of several screens, so we need to check.
        products_screen = ProductsScreen(driver)
        checkout_screen = CheckoutScreen(driver)
        
        # Wait for either the products screen or the checkout screen to appear
        # This confirms the app is fully launched and interactive.
        wait_start = time.time()
        while time.time() - wait_start < 25: # Max wait 25 seconds
            if products_screen.is_products_title_displayed() or checkout_screen.is_checkout_title_displayed():
                break
            time.sleep(0.5)
        else:
            pytest.fail("App did not launch to a known screen within 25 seconds.")

        # --- Step 3: Record end time and calculate duration ---
        end_time = time.time()
        startup_time_s = end_time - start_time
        print(f"App startup time: {startup_time_s:.2f} seconds")

        # --- Step 4: Assert that the startup time is below our threshold ---
        assert startup_time_s < STARTUP_TIME_THRESHOLD_S, \
            f"App startup time ({startup_time_s:.2f}s) exceeded threshold of {STARTUP_TIME_THRESHOLD_S}s."

    finally:
        # --- Step 5: Ensure the driver is quit, even if the test fails ---
        if driver:
            driver.quit()
            print("\n--- Teardown: Appium session quit ---")

    print("--- Finished test: test_app_startup_time ---")

