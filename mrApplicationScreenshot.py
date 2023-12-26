# pip install pygetwindow

import time
import pygetwindow as gw

def take_screenshot(window_title, file_path):
    # Wait for a moment to ensure the application is visible
    time.sleep(2)

    # Find the application window by title
    app_window = gw.getWindowsWithTitle(window_title)

    if app_window:
        # Activate the application window
        app_window[0].activate()

        # Capture the screen of the active window
        screenshot = gw.getWindowsWithTitle(window_title)[0].screenshot()

        # Add a timestamp to the file name
        timestamp = time.strftime('%Y%m%d%H%M%S')
        file_name = f'desktop_screenshot_{timestamp}.png'

        # Save the screenshot with the updated file name
        screenshot.save(file_path + file_name)
        print(f'Screenshot saved to: {file_path}{file_name}')
    else:
        print(f'Error: Window with title "{window_title}" not found.')

if __name__ == "__main__":
    # Set the file path where you want to save the screenshots
    screenshot_path = r'C:\Users\cader\OneDrive\Desktop\MRScreenShotTesting'

    # Specify the title of the application window
    # You can find the window title using gw.getAllTitles()
    window_title = 'Google Chrome'

    take_screenshot(window_title, screenshot_path)
