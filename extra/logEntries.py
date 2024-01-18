# This is temporary

import datetime

def log_time_entry(file_path):
    # Get the current date and time
    current_time = datetime.datetime.now()

    # Format the date and time as a string
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

    # Log entry with timestamp
    log_entry = f'{formatted_time} - Time entry description\n'

    # Write the log entry to the file
    with open(file_path, 'a') as file:
        file.write(log_entry)

    print(f'Time entry logged: {log_entry}')

if __name__ == "__main__":
    # Set the file path for the time log
    log_file_path = 'path_to_save_log/time_log.txt'

    # Log a time entry
    log_time_entry(log_file_path)
