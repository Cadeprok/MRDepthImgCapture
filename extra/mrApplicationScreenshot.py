# pip install pygetwindow pyautogui


# MAKE SURE YOU ARE ON CORRECT TAB
# MAKE SURE YOU ARE ON CORRECT TAB
# MAKE SURE YOU ARE ON CORRECT TAB
# MAKE SURE YOU ARE ON CORRECT TAB



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
        complete = (file_path + file_name)
        # Save the screenshot with the updated file name
        screenshot.save(complete)
        print(f'Screenshot saved to: {file_path}{file_name}')
        log_time_entry(complete)
    else:
        print(f'Error: Window with title "{window_title}" not found.')

def log_time_entry(name):
    # Get the current date and time
    file_path = "C:\Users\cader\OneDrive\Desktop\JS-Practice\MRDepthImgCapture"
    current_time = datetime.datetime.now()

    # Format the date and time as a string
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

    # Log entry with timestamp
    log_entry = name + " " + f'{formatted_time} - Time entry description\n'

    # Write the log entry to the file
    with open(file_path, 'a') as file:
        file.write(log_entry)

    print(f'Time entry logged: {log_entry}')

if __name__ == "__main__":
    # Set the file path where you want to save the screenshots
    screenshot_path = r'C:\Users\cader\OneDrive\Desktop\MRScreenShotTesting\Test1'

    # Specify the title of the application window
    # You can find the window title using gw.getAllTitles()
    window_title = 'Tigz - Twitch - Google Chrome'

    take_screenshot(window_title, screenshot_path)






# screenshot_path = r'C:\Users\cader\OneDrive\Desktop\MRScreenShotTesting\Test1'