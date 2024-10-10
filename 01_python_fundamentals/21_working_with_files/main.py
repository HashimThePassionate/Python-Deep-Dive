import os
from datetime import datetime

def read_logs(file_path):
    """Reads the existing log file and returns its content."""
    try:
        with open(file_path, 'r') as log_file:
            logs = log_file.readlines()
            print("Existing Logs:")
            for log in logs:
                print(log.strip())
            return logs
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return []

def append_log(file_path, log_message):
    """Appends a new log entry to the log file."""
    with open(file_path, 'a') as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {log_message}\n")
    print(f"Log entry added: [{timestamp}] {log_message}")

def write_backup(file_path, backup_path, logs):
    """Writes all the logs into a backup file."""
    with open(backup_path, 'w') as backup_file:
        backup_file.writelines(logs)
    print(f"Backup file '{backup_path}' created successfully.")

def main():
    log_file_path = 'logs.txt'
    backup_file_path = 'logs_backup.txt'

    # Step 1: Read existing logs
    logs = read_logs(log_file_path)

    # Step 2: Add new log entries
    append_log(log_file_path, "User logged in")
    append_log(log_file_path, "User updated settings")

    # Step 3: Read logs again after appending new entries
    logs = read_logs(log_file_path)

    # Step 4: Write logs to a backup file
    write_backup(log_file_path, backup_file_path, logs)

if __name__ == "__main__":
    main()
