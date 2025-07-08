# utils/driver_factory.py

from appium import webdriver
from appium.options.android import UiAutomator2Options
from config import APPIUM_SERVER_URL, ANDROID_CAPS

def get_android_driver():
    """
    Initializes and returns the Appium driver for Android.

    This function creates an instance of the Appium driver by combining the
    server URL with the desired capabilities specified in the config file.

    Returns:
        appium.webdriver.webdriver.WebDriver: The initialized Appium driver instance.
    """
    # The UiAutomator2Options class allows us to easily set capabilities
    options = UiAutomator2Options().load_capabilities(ANDROID_CAPS)

    print("--- Starting Appium session ---")
    print(f"Server URL: {APPIUM_SERVER_URL}")
    print(f"Capabilities: {ANDROID_CAPS}")

    try:
        driver = webdriver.Remote(
            command_executor=APPIUM_SERVER_URL,
            options=options
        )
        print("--- Appium session started successfully ---")
        return driver
    except Exception as e:
        print(f"!!! FAILED to start Appium session: {e}")
        # In case of failure, it's good practice to exit or raise the exception
        # so the tests don't proceed with an invalid driver.
        raise

