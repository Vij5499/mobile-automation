# config.py

import os

# --- Appium Server Configuration ---
# The default URL where the Appium server is running.
APPIUM_SERVER_URL = "http://127.0.0.1:4723"

# --- Desired Capabilities for Android ---
# This dictionary contains the configuration for the Android app.
ANDROID_CAPS = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "Medium Phone",  # Can be any name, but should match your running emulator
    "app": os.path.abspath("C:/Users/vijet/sauce-demo-automation/apps/Android-MyDemoAppRN.1.3.0.build-244.apk"),
    "appPackage": "com.saucelabs.mydemoapp.rn",
    "appWaitActivity": ".MainActivity",
    "autoGrantPermissions": True,
    
    # --- NEW: Capability to enable performance data collection ---
    "enablePerformanceLogging": True,
}
