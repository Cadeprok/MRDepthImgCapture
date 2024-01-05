# pip install pygetwindow pyautogui

import time
import pygetwindow as gw
import pyautogui

def take_screenshot(window_title, file_path):
    # Wait for a moment to ensure the application is visible
    time.sleep(2)

    # Find the application window by title
    app_window = gw.getWindowsWithTitle(window_title)

    if app_window:
        # Get the window's position and size using pygetwindow
        window_rect = app_window[0]._rect

        # Capture the screen of the specified window using pyautogui
        screenshot = pyautogui.screenshot(region=(window_rect.left, window_rect.top, window_rect.width, window_rect.height))

        # Add a timestamp to the file name
        timestamp = time.strftime('%Y%m%d%H%M%S')
        file_name = f'{window_title}_screenshot_{timestamp}.png'

        # Save the screenshot with the updated file name
        screenshot.save(file_path + file_name)
        print(f'Screenshot saved to: {file_path}{file_name}')
    else:
        print(f'Error: Window with title "{window_title}" not found.')

if __name__ == "__main__":
    # Set the file path where you want to save the screenshots
    screenshot_path = r'C:\Users\cader\OneDrive\Desktop\MRScreenShotTesting\Test1'

    # Specify the title of the application window
    # You can find the window title using gw.getAllTitles()
    window_title = 'Tigz - Twitch - Google Chrome'

    take_screenshot(window_title, screenshot_path)






# screenshot_path = r'C:\Users\cader\OneDrive\Desktop\MRScreenShotTesting\Test1'