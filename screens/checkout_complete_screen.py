# screens/checkout_complete_screen.py

from appium.webdriver.common.appiumby import AppiumBy
from .base_screen import BaseScreen

class CheckoutCompleteScreen(BaseScreen):
    """
    This class represents the final Checkout Complete screen.
    """

    # --- Locators ---
    _complete_title = (AppiumBy.XPATH, "//android.widget.TextView[@text='Checkout Complete']")

    def is_checkout_complete_title_displayed(self):
        """Verifies if the 'Checkout Complete' title is visible."""
        print("Checking for 'Checkout Complete' title...")
        return self.is_element_displayed(self._complete_title)

