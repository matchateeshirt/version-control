# src/main.py

import datetime

# Get the current date and time in the desired format
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Specify the file path for version.md
file_path = 'version.md'

# Write the current date and time to the file
with open(file_path, 'w') as f:
    f.write(f'Current Date and Time: {current_datetime}\n')
