import json
import re

with open(r"C:\Users\default.DESKTOP-MOGIHTS\Documents\hamsa\panchang_data.json", "r") as file:
    text = file.read()
date = r'"date"\s*:\s*"(\d{2}/\d{2}/\d{4})"'

dates= re.findall(date,text)

for d in dates:
    print(d)