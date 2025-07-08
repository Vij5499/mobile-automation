# screens/base_screen.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BaseScreen:
    """
    The BaseScreen class is a parent class for all other screen objects.
    It contains common methods that are shared across different screens.
    """

    def __init__(self, driver):
        """
        Initializes the BaseScreen object.
        """
        self.driver = driver
        # A long, robust timeout for actual interactions
        self.default_timeout = 10

    def _wait_for_element(self, locator, timeout):
        """
        Generic wait method that waits for an element to be visible.
        Accepts a custom timeout.
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            # We let the calling function handle the exception.
            raise

    def tap_element(self, locator):
        """
        Finds an element by waiting for it to be clickable, then taps it.
        Uses the default long timeout for robustness.
        """
        try:
            wait = WebDriverWait(self.driver, self.default_timeout)
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            print(f"Error: Element with locator {locator} not clickable after {self.default_timeout}s.")
            raise

    def send_keys_to_element(self, locator, text):
        """
        Finds an element by waiting for it to be visible, then sends keys to it.
        Uses the default long timeout for robustness.
        """
        try:
            element = self._wait_for_element(locator, self.default_timeout)
            element.send_keys(text)
        except TimeoutException:
            print(f"Error: Element with locator {locator} not visible after {self.default_timeout}s.")
            raise

    def is_element_displayed(self, locator, timeout=1):
        """
        A quick check to see if an element is displayed.
        Uses a very short timeout by default, ideal for state checking.
        This prevents long waits when an element is not present.
        """
        try:
            # Use a very short timeout for the check
            self._wait_for_element(locator, timeout)
            return True
        except TimeoutException:
            return False

