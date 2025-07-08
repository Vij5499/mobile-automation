# screens/login_screen.py

from appium.webdriver.common.appiumby import AppiumBy
from .base_screen import BaseScreen

class LoginScreen(BaseScreen):
    """
    This class represents the Login Screen and inherits from BaseScreen.
    """

    # --- Locators ---
    _username_input = (AppiumBy.ACCESSIBILITY_ID, "Username input field")
    _password_input = (AppiumBy.ACCESSIBILITY_ID, "Password input field")
    _login_button = (AppiumBy.ACCESSIBILITY_ID, "Login button")
    _error_message_container = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='generic-error-message']/android.widget.TextView")


    def enter_username(self, username):
        """Waits for the username input field and types the given username."""
        print(f"Entering username: '{username}'")
        self.send_keys_to_element(self._username_input, username)

    def enter_password(self, password):
        """Waits for the password input field and types the given password."""
        print(f"Entering password: '{password}'")
        self.send_keys_to_element(self._password_input, password)

    def tap_login_button(self):
        """Waits for the login button and then taps it."""
        print("Tapping login button")
        self.tap_element(self._login_button)

    def is_error_message_displayed(self):
        """Verifies if the generic error message is visible using a quick check."""
        print("Checking for login error message...")
        # Use the new, fast checking method from BaseScreen
        return self.is_element_displayed(self._error_message_container)

