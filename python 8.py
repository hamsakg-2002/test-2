import re
from datetime import datetime

with open(r"C:\Users\default.DESKTOP-MOGIHTS\Documents\hamsa\panchang_data.json", "r", encoding="utf-8") as file:
    text = file.read()

date_pattern = r'"date"\s*:\s*"(\d{2}/\d{2}/\d{4})"'
dates = re.findall(date_pattern, text)

time_pattern = r'"([0-2]?\d:[0-5]\d)"'
times = re.findall(time_pattern, text)

date_time_dict = dict(zip(dates, times))

# Normal function instead of lambda
def sort_by_date(item):
    return datetime.strptime(item[0], "%d/%m/%Y")

# Sort dictionary
sorted_date_time = dict(sorted(date_time_dict.items(), key=sort_by_date))

# Print output
for d, t in sorted_date_time.items():
    print(d, ":", t)
