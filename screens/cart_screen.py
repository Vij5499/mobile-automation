# screens/cart_screen.py

from appium.webdriver.common.appiumby import AppiumBy
from .base_screen import BaseScreen
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CartScreen(BaseScreen):
    """
    This class represents the Shopping Cart screen.
    """

    # --- Locators ---
    _cart_title = (AppiumBy.XPATH, "//android.widget.TextView[@text='My Cart']")
    _backpack_item = (AppiumBy.XPATH, "//android.widget.TextView[@text='Sauce Labs Backpack']")
    _quantity_increase_button = (AppiumBy.ACCESSIBILITY_ID, "counter plus button")
    _quantity_decrease_button = (AppiumBy.ACCESSIBILITY_ID, "counter minus button")
    _remove_item_button = (AppiumBy.ACCESSIBILITY_ID, "remove item")
    _cart_quantity_text = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='cart badge']/android.widget.TextView")
    _proceed_to_checkout_button = (AppiumBy.ACCESSIBILITY_ID, "Proceed To Checkout button")
    _no_items_text = (AppiumBy.XPATH, "//android.widget.TextView[@text='No Items']")

    # --- FIX: Using more specific parent-child XPath locators for prices ---
    _backpack_price = (AppiumBy.XPATH, "//android.widget.TextView[@text='Sauce Labs Backpack']/../android.widget.TextView[starts-with(@text, '$')]")
    _bike_light_price = (AppiumBy.XPATH, "//android.widget.TextView[@text='Sauce Labs Bike Light']/../android.widget.TextView[starts-with(@text, '$')]")
    _total_price = (AppiumBy.ACCESSIBILITY_ID, "total price")


    def wait_for_screen_to_load(self):
        """Waits for the 'My Cart' title to be visible."""
        print("Waiting for cart screen to load...")
        self._wait_for_element(self._cart_title, 5)

    def is_backpack_in_cart(self):
        """Verifies if the Sauce Labs Backpack is visible in the cart."""
        print("Checking for backpack in cart...")
        return self.is_element_displayed(self._backpack_item, timeout=5)

    def increase_quantity(self):
        """Taps the '+' button to increase the item quantity."""
        print("Increasing item quantity")
        self.tap_element(self._quantity_increase_button)

    def decrease_quantity(self):
        """Taps the '-' button to decrease the item quantity."""
        print("Decreasing item quantity")
        self.tap_element(self._quantity_decrease_button)

    def remove_item(self):
        """Taps the 'Remove Item' button."""
        print("Removing item from cart")
        self.tap_element(self._remove_item_button)

    def get_cart_quantity(self):
        """Gets the text representing the total number of items in the cart icon."""
        print("Getting cart quantity from badge")
        try:
            element = self._wait_for_element(self._cart_quantity_text, 5)
            return element.text
        except:
            print("Could not find cart quantity text.")
            return None
            
    def proceed_to_checkout(self):
        """Taps the 'Proceed To Checkout' button."""
        print("Proceeding to checkout")
        self.tap_element(self._proceed_to_checkout_button)

    def is_cart_empty(self):
        """Verifies if the 'No Items' message is displayed."""
        print("Checking if cart is empty...")
        return self.is_element_displayed(self._no_items_text)

    def is_checkout_button_displayed(self):
        """Verifies if the 'Proceed To Checkout' button is displayed."""
        print("Checking for 'Proceed To Checkout' button...")
        return self.is_element_displayed(self._proceed_to_checkout_button)

    def wait_for_cart_quantity_to_be(self, quantity_str):
        """
        Waits for the cart quantity badge to display a specific number.
        """
        print(f"Waiting for cart quantity to be '{quantity_str}'")
        try:
            wait = WebDriverWait(self.driver, self.default_timeout)
            wait.until(EC.text_to_be_present_in_element(self._cart_quantity_text, quantity_str))
            return True
        except:
            print(f"Cart quantity did not update to '{quantity_str}' in time.")
            return False

    def get_backpack_price(self):
        """Gets the price text of the backpack."""
        return self._wait_for_element(self._backpack_price, 5).text

    def get_bike_light_price(self):
        """Gets the price text of the bike light."""
        return self._wait_for_element(self._bike_light_price, 5).text

    def get_total_price(self):
        """Gets the total price text."""
        return self._wait_for_element(self._total_price, 5).text

