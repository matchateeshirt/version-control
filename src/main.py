import datetime

current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

file_path = 'version.md'

with open(file_path, 'w') as f:
    f.write(f'Current Date and Time: {current_datetime}\n')
