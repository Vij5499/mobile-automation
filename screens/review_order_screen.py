# screens/review_order_screen.py

from appium.webdriver.common.appiumby import AppiumBy
from .base_screen import BaseScreen

class ReviewOrderScreen(BaseScreen):
    """
    This class represents the Review Your Order screen.
    """

    # --- Locators ---
    _place_order_button = (AppiumBy.ACCESSIBILITY_ID, "Place Order button")

    def tap_place_order_button(self):
        """Taps the 'Place Order' button."""
        print("Tapping 'Place Order' button")
        self.tap_element(self._place_order_button)

