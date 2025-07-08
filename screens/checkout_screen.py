# screens/checkout_screen.py

from appium.webdriver.common.appiumby import AppiumBy
from .base_screen import BaseScreen

class CheckoutScreen(BaseScreen):
    """
    This class represents the Checkout / Shipping Address screen.
    It now includes methods for reading form validation errors.
    """

    # --- Locators ---
    _screen_title = (AppiumBy.XPATH, "//android.widget.TextView[@text='Enter a shipping address']")
    _menu_button = (AppiumBy.ACCESSIBILITY_ID, "open menu")
    _catalog_menu_item = (AppiumBy.ACCESSIBILITY_ID, "menu item catalog")

    # --- Locators for shipping form ---
    _full_name_input = (AppiumBy.ACCESSIBILITY_ID, "Full Name* input field")
    _address_line_1_input = (AppiumBy.ACCESSIBILITY_ID, "Address Line 1* input field")
    _city_input = (AppiumBy.ACCESSIBILITY_ID, "City* input field")
    _zip_code_input = (AppiumBy.ACCESSIBILITY_ID, "Zip Code* input field")
    _country_input = (AppiumBy.ACCESSIBILITY_ID, "Country* input field")
    _to_payment_button = (AppiumBy.ACCESSIBILITY_ID, "To Payment button")

    # --- NEW: Locators for error messages ---
    _full_name_error_text = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='Full Name*-error-message']/android.widget.TextView")
    _address_line_1_error_text = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='Address Line 1*-error-message']/android.widget.TextView")


    def is_checkout_title_displayed(self):
        """Verifies if the 'Enter a shipping address' title is visible."""
        print("Checking for Checkout screen title...")
        return self.is_element_displayed(self._screen_title)

    def navigate_to_catalog(self):
        """Navigates from the checkout screen to the product catalog."""
        print("Navigating to product catalog...")
        self.tap_element(self._menu_button)
        self.tap_element(self._catalog_menu_item)
        
    def fill_shipping_address(self, name, address, city, zip_code, country):
        """Fills out the entire shipping address form."""
        print("Filling shipping address...")
        self.send_keys_to_element(self._full_name_input, name)
        self.send_keys_to_element(self._address_line_1_input, address)
        self.send_keys_to_element(self._city_input, city)
        self.send_keys_to_element(self._zip_code_input, zip_code)
        self.send_keys_to_element(self._country_input, country)

    def tap_to_payment_button(self):
        """Taps the 'To Payment' button."""
        print("Tapping 'To Payment' button")
        self.tap_element(self._to_payment_button)

    def get_full_name_error(self):
        """Gets the error text for the full name field."""
        print("Getting full name error text")
        try:
            element = self._wait_for_element(self._full_name_error_text, 5)
            return element.text
        except:
            print("Could not find the full name error message.")
            return None

    def get_address_error(self):
        """Gets the error text for the address line 1 field."""
        print("Getting address error text")
        try:
            element = self._wait_for_element(self._address_line_1_error_text, 5)
            return element.text
        except:
            print("Could not find the address error message.")
            return None

