# tests/test_accessibility.py

import pytest
from screens.login_screen import LoginScreen
from screens.products_screen import ProductsScreen

@pytest.mark.accessibility
def test_login_screen_accessibility_labels(driver):
    """
    This accessibility test verifies that all key interactive elements
    on the login screen have a content-description (accessibility label).
    """
    print("--- Starting test: test_login_screen_accessibility_labels ---")

    # --- Step 1: Ensure we are on the Login screen ---
    products_screen = ProductsScreen(driver)
    if products_screen.is_products_title_displayed():
        print("User is already logged in. Performing logout first.")
        products_screen.perform_logout()

    login_screen = LoginScreen(driver)
    
    # --- Step 2: Iterate through key elements and check their labels ---
    elements_to_check = login_screen.key_elements
    
    for locator in elements_to_check:
        try:
            # Find the element using the base screen's wait method
            element = login_screen._wait_for_element(locator, 5)
            # Get the content-desc attribute
            content_desc = element.get_attribute('content-desc')
            print(f"Checking element with locator {locator}. Found content-desc: '{content_desc}'")
            
            # Assert that the content-desc is not None and not an empty string
            assert content_desc, f"Element with locator {locator} has no content-desc attribute."
            assert content_desc.strip() != "", f"Element with locator {locator} has an empty content-desc."

        except Exception as e:
            pytest.fail(f"Failed to find or check element with locator {locator}. Error: {e}")

    print("--- Finished test: test_login_screen_accessibility_labels ---")

