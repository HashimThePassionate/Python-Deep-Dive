# File: main.py

import sys
import os

# Get the current directory (where main.py is located)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory (up one level)
parent_dir = os.path.dirname(os.path.dirname(current_dir))

# Construct the path to 'common_utils'
common_utils_path = os.path.join(parent_dir, 'common_utils')

# Add 'common_utils' to sys.path if it's not already there
if common_utils_path not in sys.path:
    sys.path.append(common_utils_path)

# Now we can import modules from 'common_utils'
from mypackage import my_module
import helper  # Importing from 'common_utils' directory

def main():
    name = helper.get_name()
    my_module.greet(name)
    my_module.farewell(name)

if __name__ == "__main__":
    main()
