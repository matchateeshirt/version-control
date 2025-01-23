from datetime import datetime

now = datetime.now()

current_time = now.strftime("%Y-%m-%d %H:%M:%S")

with open("../version.md", "w") as file:
    file.write(f"Last updated: {current_time}\n")

print(f"Current time written to version.md: {current_time}")
