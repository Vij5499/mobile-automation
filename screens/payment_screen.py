# screens/payment_screen.py

from appium.webdriver.common.appiumby import AppiumBy
from .base_screen import BaseScreen

class PaymentScreen(BaseScreen):
    """
    This class represents the Payment Method screen.
    """

    # --- Locators ---
    _full_name_input = (AppiumBy.XPATH, "//android.view.ViewGroup[.//android.widget.TextView[@text='Enter a payment method']]//android.widget.EditText[@content-desc='Full Name* input field']")
    _card_number_input = (AppiumBy.ACCESSIBILITY_ID, "Card Number* input field")
    _expiration_date_input = (AppiumBy.ACCESSIBILITY_ID, "Expiration Date* input field")
    _security_code_input = (AppiumBy.ACCESSIBILITY_ID, "Security Code* input field")
    _review_order_button = (AppiumBy.ACCESSIBILITY_ID, "Review Order button")
    # --- NEW: Locator for card number error message ---
    _card_number_error_text = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='Card Number*-error-message']/android.widget.TextView")


    def fill_payment_details(self, name, card_number, expiration, security_code):
        """Fills out the entire payment details form."""
        print("Filling payment details...")
        self.send_keys_to_element(self._full_name_input, name)
        self.send_keys_to_element(self._card_number_input, card_number)
        self.send_keys_to_element(self._expiration_date_input, expiration)
        self.send_keys_to_element(self._security_code_input, security_code)
        # It's good practice to hide the keyboard after typing
        self.driver.hide_keyboard()

    def tap_review_order_button(self):
        """
        Taps the 'Review Order' button.
        Taps the button twice to work around an app bug.
        """
        print("Tapping 'Review Order' button (first attempt)")
        self.tap_element(self._review_order_button)
        print("Tapping 'Review Order' button (second attempt to workaround bug)")
        self.tap_element(self._review_order_button)

    def get_card_number_error(self):
        """Gets the error text for the card number field."""
        print("Getting card number error text")
        try:
            element = self._wait_for_element(self._card_number_error_text, 5)
            return element.text
        except:
            print("Could not find the card number error message.")
            return None

