import os
import random
from datetime import datetime, timedelta

# Define start and end dates
start_date = datetime(2023, 2, 7)
end_date = datetime(2024, 5, 15)

# Generate all dates in the range
delta = (end_date - start_date).days
dates = [start_date + timedelta(days=i) for i in range(delta + 1)]

# Loop over each date
for date in dates:
    for _ in range(random.randint(1, 3)):  # 1 to 3 commits per day
        d_str = date.strftime("%Y-%m-%d %H:%M:%S")
        
        with open("file.txt", "a") as file:
            file.write(d_str + "\n")
        
        os.system("git add .")
        os.system(f'git commit --date="{d_str}" -m "commit"')

os.system('git push -u origin main')