# screens/product_details_screen.py

from appium.webdriver.common.appiumby import AppiumBy
from .base_screen import BaseScreen

class ProductDetailsScreen(BaseScreen):
    """
    This class represents the Product Details screen, which is displayed
    after tapping on a product from the catalog.
    """

    # --- Locators ---
    _add_to_cart_button = (AppiumBy.ACCESSIBILITY_ID, "Add To Cart button")

    def add_to_cart(self):
        """
        Taps the 'Add To Cart' button on the product details page.
        """
        print("Tapping 'Add To Cart' on the details page")
        self.tap_element(self._add_to_cart_button)

