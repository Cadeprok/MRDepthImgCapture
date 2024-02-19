# pip install pyautogui

import time
import datetime
import pyautogui

def take_screenshot(file_path, left, top, width, height, n):
    # Wait for a moment to ensure the application is visible
    time.sleep(0.40)

    # Capture the specified region of the screen using pyautogui
    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    # Add a timestamp to the file name
    timestamp = time.strftime('%Y%m%d%H%M%S')
    file_name = f'screenshot_{timestamp}.png'
    addition = f'_ {n} _'
    complete = (file_path + addition + file_name)

    # Save the screenshot with the updated file name
    screenshot.save(complete)
    print(f'Screenshot saved to: {complete}')
    log_time_entry(n)
    time.sleep(0.45)

def log_time_entry(n):
    # Get the current date and time
    file_path = r'C:\Users\cader\OneDrive\Desktop\Depth-Data\Pose-2-Time-T2.txt'
    # file_path = r'C:\Users\cader\OneDrive\Desktop\Test11\t2.txt' # THIS IS FOR TESTING!!!
    current_time = datetime.datetime.now()

    # Format the date and time as a string
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

    # Log entry with timestamp
    log_entry = f'{formatted_time} - {n} \n'

    # Write the log entry to the file
    with open(file_path, 'a') as file:
        file.write(log_entry)

    print(f'Time entry logged: {log_entry}')

if __name__ == "__main__":
    # Set the file path where you want to save the screenshots
    screenshot_path = r'C:\Users\cader\OneDrive\Desktop\Depth-Data\Pose-2-T2\Take2_'
    #screenshot_path = r'C:\Users\cader\OneDrive\Desktop\Test11\Test1111111_' # THIS IS FOR TESTING
    # Specify the coordinates for the region you want to capture
    left = 12
    top = 50
    width = 750  # Adjust the width as needed
    height = 750  # Adjust the height as needed

    for i in range(0,1000): # MAKE SURE THIS IS CORRECT
        take_screenshot(screenshot_path, left, top, width, height, i)
