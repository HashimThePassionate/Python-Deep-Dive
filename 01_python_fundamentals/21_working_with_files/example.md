# 📝 **Scenario**: A Log Management System

In this example, we will:

1. Read from an existing log file (`logs.txt`).
2. Append new log entries to the log file.
3. Handle any errors, such as missing files.
4. Write the entire log file contents to another backup file (`logs_backup.txt`).
5. Use the `with` statement to ensure files are properly closed.


### 📄 **The Log Manager Code**

```python
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
```


### 📖 **Explanation of the Code**

#### **1. Reading Logs from a File**
The `read_logs()` function tries to open the log file (`logs.txt`) in **read mode** (`'r'`). If the file exists, it reads all the lines and prints them. If the file doesn’t exist, it catches the **FileNotFoundError** and returns an empty list.

#### **2. Appending New Log Entries**
The `append_log()` function opens the log file in **append mode** (`'a'`) and adds a new log entry with a **timestamp**. The `datetime.now().strftime()` function is used to format the timestamp.

#### **3. Writing a Backup**
The `write_backup()` function writes all the existing logs into a **backup file** (`logs_backup.txt`) using **write mode** (`'w'`), which creates or overwrites the backup file.

#### **4. The `with` Statement**
Each file operation uses the `with` statement, ensuring that the files are properly **closed** after the block of code completes.


### 📋 **Sample Run Output**

```
Error: The file 'logs.txt' does not exist.
Log entry added: [2024-10-08 14:30:15] User logged in
Log entry added: [2024-10-08 14:31:45] User updated settings
Existing Logs:
[2024-10-08 14:30:15] User logged in
[2024-10-08 14:31:45] User updated settings
Backup file 'logs_backup.txt' created successfully.
```


### 📂 **How the Log Files Look**

#### **logs.txt** (after adding new entries):
```
[2024-10-08 14:30:15] User logged in
[2024-10-08 14:31:45] User updated settings
```

#### **logs_backup.txt**:
```
[2024-10-08 14:30:15] User logged in
[2024-10-08 14:31:45] User updated settings
```


### 🛠️ **How to Run the Program**

1. If the `logs.txt` file doesn’t exist, it will show an error (FileNotFoundError) and create one by appending new logs.
2. Every time the program runs, it appends new log entries.
3. It creates a **backup file** (`logs_backup.txt`) containing the full contents of `logs.txt`.


### 🔧 **Features and Error Handling**

- **Error handling**: The code catches **FileNotFoundError** when trying to read a non-existent file and handles it gracefully by printing an error message.
- **File management**: It uses the `with` statement to ensure files are properly closed, avoiding resource leaks.
- **Appending and writing**: New log entries are appended, and the entire log file is written to a backup file.


### 🌟 **Key Takeaways**

- **Reading files** with `open('file', 'r')`.
- **Appending data** to a file with `open('file', 'a')`.
- **Writing files** with `open('file', 'w')`.
- Handling **FileNotFoundError** to ensure the program doesn’t crash when files are missing.
- Using the `with` statement for **safe file handling**.
- Managing **log data** and keeping a **backup** of logs in a separate file.

