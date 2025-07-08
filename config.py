# config.py

import os

# --- Appium Server Configuration ---
# The default URL where the Appium server is running.
APPIUM_SERVER_URL = "http://127.0.0.1:4723"

# --- Desired Capabilities for Android ---
# This dictionary contains the configuration for the Android app.
#
# Note: iOS testing requires a macOS machine to run Xcode and the iOS Simulator.
# We are focusing on Android for this project as it can be fully developed on Windows.
ANDROID_CAPS = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "Medium Phone",  # Can be any name, but should match your running emulator
    # This is the path to your app file.
    "app": os.path.abspath("C:/Users/vijet/sauce-demo-automation/apps/Android-MyDemoAppRN.1.3.0.build-244.apk"),
    
    # --- FIX ---
    # Added the correct appPackage and changed appWaitActivity.
    # This tells Appium the unique identifier of the app and which screen to wait for.
    "appPackage": "com.saucelabs.mydemoapp.rn",
    "appWaitActivity": ".MainActivity",
    
    "autoGrantPermissions": True, # Automatically grant app permissions
}
