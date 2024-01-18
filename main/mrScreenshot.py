# This is to take an image of the entire screen. 


import time
import pyautogui

def take_screenshot(file_path):
    # Wait for a moment to ensure the application is visible
    time.sleep(2)

    # Capture the screen
    screenshot = pyautogui.screenshot()

    # Add a timestamp to the file name
    timestamp = time.strftime('%Y%m%d%H%M%S')
    file_name = f'desktop_screenshot_{timestamp}.png'

    # Save the screenshot with the updated file name
    screenshot.save(file_path + file_name)
    print(f'Screenshot saved to: {file_path}{file_name}')

if __name__ == "__main__":
    # Path will need to be changed depending on what system you are using (Desktop @ lab, personal, etc)
    # Set the file path where you want to save the screenshots
    screenshot_path = r"C:\Users\cader\OneDrive\Desktop\MRScreenShotTesting"

    # Number of screenshots to capture
    num_screenshots = 5

    for _ in range(num_screenshots):
        take_screenshot(screenshot_path)



# How to run the script:
# 'cd' into script path 
# python3 filename.py
