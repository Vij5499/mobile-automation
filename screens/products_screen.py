# screens/products_screen.py

from appium.webdriver.common.appiumby import AppiumBy
from .base_screen import BaseScreen

class ProductsScreen(BaseScreen):
    """
    This class represents the Products Screen.
    """

    # --- Locators ---
    _products_title = (AppiumBy.XPATH, "//android.widget.TextView[@text='Products']")
    _menu_button = (AppiumBy.ACCESSIBILITY_ID, "open menu")
    _logout_menu_item = (AppiumBy.ACCESSIBILITY_ID, "menu item log out")
    _logout_confirm_button = (AppiumBy.ID, "android:id/button1")
    _logout_ok_button = (AppiumBy.ID, "android:id/button1")
    _backpack_item = (AppiumBy.XPATH, "//android.widget.TextView[@text='Sauce Labs Backpack']")
    # --- NEW: Locator for the second item ---
    _bike_light_item = (AppiumBy.XPATH, "//android.widget.TextView[@text='Sauce Labs Bike Light']")
    _cart_icon = (AppiumBy.ACCESSIBILITY_ID, "cart badge")
    _sort_button = (AppiumBy.ACCESSIBILITY_ID, "sort button")
    _price_asc_option = (AppiumBy.XPATH, "//android.widget.TextView[@text='Price - Ascending']")
    _price_desc_option = (AppiumBy.XPATH, "//android.widget.TextView[@text='Price - Descending']")
    _first_item_price = (AppiumBy.XPATH, "(//android.view.ViewGroup[@content-desc='store item'])[1]//android.widget.TextView[starts-with(@text, '$')]")


    def is_products_title_displayed(self):
        """Verifies if the 'Products' title is visible using a quick check."""
        print("Checking for Products screen title...")
        return self.is_element_displayed(self._products_title)

    def perform_logout(self):
        """Executes the complete logout sequence."""
        print("--- Starting full logout sequence ---")
        self.tap_element(self._menu_button)
        self.tap_element(self._logout_menu_item)
        print("Tapping logout confirmation button")
        self.tap_element(self._logout_confirm_button)
        print("Tapping final OK button on success message")
        self.tap_element(self._logout_ok_button)
        print("--- Logout sequence complete ---")

    def select_backpack(self):
        """Selects the Sauce Labs Backpack to navigate to its details page."""
        print("Selecting Sauce Labs Backpack from the catalog")
        self.tap_element(self._backpack_item)

    def select_bike_light(self):
        """Selects the Sauce Labs Bike Light to navigate to its details page."""
        print("Selecting Sauce Labs Bike Light from the catalog")
        self.tap_element(self._bike_light_item)

    def tap_cart_icon(self):
        """Taps the cart icon to navigate to the cart screen."""
        print("Tapping cart icon")
        self.tap_element(self._cart_icon)

    def sort_by_price_ascending(self):
        """Taps the sort button and selects the 'Price - Ascending' option."""
        print("Sorting products by price (ascending)")
        self.tap_element(self._sort_button)
        self.tap_element(self._price_asc_option)

    def sort_by_price_descending(self):
        """Taps the sort button and selects the 'Price - Descending' option."""
        print("Sorting products by price (descending)")
        self.tap_element(self._sort_button)
        self.tap_element(self._price_desc_option)

    def get_first_item_price(self):
        """
        Gets the price text of the first item in the product list.
        """
        print("Getting price of the first item in the list")
        try:
            element = self._wait_for_element(self._first_item_price, 5)
            return element.text
        except:
            print("Could not find the price of the first item.")
            return None

