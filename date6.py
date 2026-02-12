import json
import re

with open(r"C:\Users\default.DESKTOP-MOGIHTS\Documents\hamsa\panchang_data.json", "r") as file:
    text = file.read()
date_pattern = r'"date"\s*:\s*"(\d{2}/\d{2}/\d{4})"'
dates = re.findall(date_pattern, text)
time_pattern = r'"([0-2]?\d:[0-5]\d)"'
times = re.findall(time_pattern, text)
date_time_dict = dict(zip(dates, times))
print(date_time_dict)
