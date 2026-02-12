import json
import re

with open(r"C:\Users\default.DESKTOP-MOGIHTS\Documents\hamsa\panchang_data.json", "r") as file:
    text = file.read()
end_time =r'"([0-2]?\d:[0-5]\d)"'

times = re.findall(end_time, text)

for t in times:
    print(t)
